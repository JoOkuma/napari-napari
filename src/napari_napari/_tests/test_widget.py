from napari_napari import Napari


def test_napari(make_napari_viewer):
    viewer = make_napari_viewer()
    Napari(viewer)
    assert len(viewer.layers) == 1
