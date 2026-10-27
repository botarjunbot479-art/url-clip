from pathlib import Path
import json, clip

def test_add_get(tmp_path, monkeypatch):
    monkeypatch.setattr(clip, 'DB', tmp_path/'clips.json')
    clip.save({'x':'http://a'})
    assert clip.load()['x']=='http://a'
