import pathlib
import scipy.sparse

from rasa.model_training import train_nlu
from rasa.shared.nlu.training_data.message import Message
from rasa_nlu_examples.scikit import load_interpreter


nlu_data = "tests/data/nlu/en/nlu.md"
mod = train_nlu(
    nlu_data=nlu_data,
    config="tests/configs/hyphen-config.yml",
    output="models",
)


def test_features_are_sparse():
    interpreter = load_interpreter(*pathlib.Path(mod).parts)
    msg = Message({"text": "am I talking to a bot"})
    for p in interpreter.interpreter.pipeline:
        p.process(msg)

    for feature in msg.get_sparse_features("text"):
        assert scipy.sparse.issparse(feature.features)

    feat_tok, feat_sent = msg.get_sparse_features("text")
    assert feat_tok.features.sum() == feat_sent.features.sum()
