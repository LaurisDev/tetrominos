import pytest
from modulo.modelo.tetrominos import Tetromino


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_i_rota_correctamente(rotation):
    # Arrange:
    tetromino_i = Tetromino([
        ['.', '.', '@', '.'],
        ['.', '.', '@', '.'],
        ['.', '.', '@', '.'],
        ['.', '.', '@', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_i.rotate()

    # Assert:
    assert tetromino_i.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_i.shape == ([
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['@', '@', '@', '@'],
            ['.', '.', '.', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_i.shape == ([
            ['.', '@', '.', '.'],
            ['.', '@', '.', '.'],
            ['.', '@', '.', '.'],
            ['.', '@', '.', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_i.shape == ([
            ['.', '.', '.', '.'],
            ['@', '@', '@', '@'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.']
        ])


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_o_rota_correctamente(rotation):
    # Arrange:
    tetromino_o = Tetromino([
        ['.', '.', '.', '.'],
        ['.', '@', '@', '.'],
        ['.', '@', '@', '.'],
        ['.', '.', '.', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_o.rotate()

    # Assert:
    assert tetromino_o.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_o.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '.', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_o.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '.', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_o.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '.', '.']
        ])


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_t_rota_correctamente(rotation):
    # Arrange:
    tetromino_t = Tetromino([
        ['.', '.', '.', '.'],
        ['.', '@', '@', '@'],
        ['.', '.', '@', '.'],
        ['.', '.', '.', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_t.rotate()

    # Assert:
    assert tetromino_t.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_t.shape == ([
            ['.', '.', '.', '.'],
            ['.', '.', '@', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '@', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_t.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '.', '.'],
            ['@', '@', '@', '.'],
            ['.', '.', '.', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_t.shape == ([
            ['.', '@', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '.', '.'],
            ['.', '.', '.', '.']
        ])


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_s_rota_correctamente(rotation):
    # Arrange:
    tetromino_s = Tetromino([
        ['.', '.', '.', '.'],
        ['.', '.', '@', '@'],
        ['.', '@', '@', '.'],
        ['.', '.', '.', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_s.rotate()

    # Assert:
    assert tetromino_s.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_s.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '@', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_s.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '.'],
            ['@', '@', '.', '.'],
            ['.', '.', '.', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_s.shape == ([
            ['.', '@', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '.', '.']
        ])


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_z_rota_correctamente(rotation):
    # Arrange:
    tetromino_z = Tetromino([
        ['.', '.', '.', '.'],
        ['.', '@', '@', '@'],
        ['.', '.', '@', '.'],
        ['.', '.', '.', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_z.rotate()

    # Assert:
    assert tetromino_z.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_z.shape == ([
            ['.', '.', '.', '.'],
            ['.', '.', '@', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '.', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_z.shape == ([
            ['.', '.', '.', '.'],
            ['@', '@', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '.', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_z.shape == ([
            ['.', '.', '@', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '.', '.'],
            ['.', '.', '.', '.']
        ])


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_j_rota_correctamente(rotation):
    # Arrange:
    tetromino_j = Tetromino([
        ['.', '.', '@', '.'],
        ['.', '.', '@', '.'],
        ['.', '@', '@', '.'],
        ['.', '.', '.', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_j.rotate()

    # Assert:
    assert tetromino_j.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_j.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '.', '.'],
            ['.', '@', '@', '@'],
            ['.', '.', '.', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_j.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '@', '.', '.'],
            ['.', '@', '.', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_j.shape == ([
            ['.', '.', '.', '.'],
            ['@', '@', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '.', '.']
        ])


@pytest.mark.parametrize("rotation", [1, 2, 3])
def test_tetromino_l_rota_correctamente(rotation):
    # Arrange:
    tetromino_l = Tetromino([
        ['.', '@', '.', '.'],
        ['.', '@', '.', '.'],
        ['.', '@', '@', '.'],
        ['.', '.', '.', '.']
    ])

    # Act:
    for _ in range(rotation):
        tetromino_l.rotate()

    # Assert:
    assert tetromino_l.rotation == rotation
    if rotation % 4 == 1:
        assert tetromino_l.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '@'],
            ['.', '@', '.', '.'],
            ['.', '.', '.', '.']
        ])
    elif rotation % 4 == 2:
        assert tetromino_l.shape == ([
            ['.', '.', '.', '.'],
            ['.', '@', '@', '.'],
            ['.', '.', '@', '.'],
            ['.', '.', '@', '.']
        ])

    elif rotation % 4 == 3:
        assert tetromino_l.shape == ([
            ['.', '.', '.', '.'],
            ['.', '.', '@', '.'],
            ['@', '@', '@', '.'],
            ['.', '.', '.', '.']
        ])
















