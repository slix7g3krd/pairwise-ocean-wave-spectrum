import pytest
import math
from render import ocean_fft as mod

CASES = [
    ("period", 'm.fft_period(64) == 64'),
    ("weight", 'm.direction_weight(0, 0) == approx(1.0)'),
    ("chop", 'm.choppiness(20, 1.0) == approx(1.0)'),
    ("norm", 'm.normal_scale(2, 0.5) == approx(4.0)'),
    ("phase", 'm.cascade_phase(7, 4) == 3'),
    ("absorb", 'm.absorption(2, 0.5) == approx(0.367879, rel=1e-5)'),
    ("foam", 'm.foam(1, 1, 0.5) == 1.0'),
    ("energy", 'm.spectral_energy([1, 2]) == 5'),
    ("wave", 'm.wave_height(2, math.pi / 2) == approx(2.0)'),
    ("uv", 'm.tile_uv((1.5, -0.2)) == approx((0.5, 0.8))'),
    ("norme", 'm.energy_norm(4) == approx(0.25)'),
    ("angle", 'm.wind_angle(1, 0) == approx(0.0)'),
    ("slope", 'm.wave_slope(2, 4) == approx(0.5)'),
    ("id", 'm.ocean_id(3, 2) == "3:2"'),
    ("valid", 'm.valid_uv((0.5, 0.5)) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
