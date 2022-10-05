"""
Unit tests for the SIESTAstepper library.
"""
from __future__ import absolute_import
import sys
import unittest
import os
import shutil
from SIESTAstepper import __file__ as mfile
from .testers import (
    settings,
    read_file,
    clear_temp,
    initialise_fake_project,
    fake_command,
    set_fake_project,
    get_fake_project,
    run_next_tester,
    single_run_tester,
    ani_to_fdf_tester,
    xyz_to_fdf_tester,
    xv_to_fdf_tester,
    merge_ani_tester,
    run_tester,
    run_interrupted_tester,
    single_run_interrupted_tester,
    make_directories_tester,
    copy_files_tester,
    energy_analysis_tester,
    force_analysis_tester,
    energy_diff_tester,
    force_diff_tester,
    pair_correlation_function_tester,
    get_it_tester,
    read_fdf_tester,
    create_fdf_tester,
    read_energy_tester,
    print_run_tester,
    check_restart_tester,
    check_userbasis_tester,
    copy_file_tester,
    sort__tester,
    remove_nones_tester,
    main_tester
)

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


mpath = mfile.replace("/SIESTAstepper/__init__.py", "")


def test_ani_to_fdf():
    """Tests for ani_to_fdf"""
    assert ani_to_fdf_tester(
        "{0}{1}tests{1}assets{1}ANI{1}C-4.ANI".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}fdf{1}C-0.fdf".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}temp{1}C-5.fdf".format(mpath, os.sep)
    ) == read_file("{0}{1}tests{1}assets{1}fdf{1}C-5.fdf".format(mpath, os.sep))


def test_xyz_to_fdf():
    """Tests for xyz_to_fdf"""
    assert xyz_to_fdf_tester(
        "{0}{1}tests{1}assets{1}xyz{1}C.xyz".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}fdf{1}C-0.fdf".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}temp{1}C-1.fdf".format(mpath, os.sep)
    ) == read_file("{0}{1}tests{1}assets{1}fdf{1}C-1.fdf".format(mpath, os.sep))


def test_xv_to_fdf():
    """Tests for xv_to_fdf"""
    if sys.version_info[0] == 2:
        assert xv_to_fdf_tester(
            "{0}{1}tests{1}assets{1}XV{1}C-XV-1.XV".format(mpath, os.sep),
            "{0}{1}tests{1}assets{1}fdf{1}C-XV-1.fdf".format(mpath, os.sep),
            "{0}{1}tests{1}assets{1}temp{1}C-XV-2.fdf".format(mpath, os.sep)
        ) == read_file("{0}{1}tests{1}assets{1}fdf{1}C-XV-2-py2.7.fdf".format(mpath, os.sep))
    else:
        assert xv_to_fdf_tester(
            "{0}{1}tests{1}assets{1}XV{1}C-XV-1.XV".format(mpath, os.sep),
            "{0}{1}tests{1}assets{1}fdf{1}C-XV-1.fdf".format(mpath, os.sep),
            "{0}{1}tests{1}assets{1}temp{1}C-XV-2.fdf".format(mpath, os.sep)
        ) == read_file("{0}{1}tests{1}assets{1}fdf{1}C-XV-2.fdf".format(mpath, os.sep))


def test_merge_ani():
    """Tests for merge_ani"""
    assert merge_ani_tester(label="C", folder="Carbon") == read_file(
        "{0}{1}tests{1}assets{1}ANI{1}C-merged.ANI".format(mpath, os.sep)
    )


def test_make_directories():
    """Tests for make_directories"""
    if not os.path.isdir("{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep)):
        os.mkdir("{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep))
    os.chdir("{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep))
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]


def test_copy_files():
    """Tests for copy_files"""
    assert copy_files_tester(
        ["psf", "DM", "XV"], "C",
        "{0}{1}tests{1}assets{1}runs{1}Carbon{1}i1".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}temp{1}Carbon{1}i2".format(mpath, os.sep)
    ) == [
               "{0}{1}tests{1}assets{1}temp{1}Carbon{1}i2{1}C.psf".format(mpath, os.sep),
               "{0}{1}tests{1}assets{1}temp{1}Carbon{1}i2{1}C.DM".format(mpath, os.sep),
               "{0}{1}tests{1}assets{1}temp{1}Carbon{1}i2{1}C.XV".format(mpath, os.sep)
           ]


def test_energy_analysis():
    """Tests for energy_analysis"""
    assert energy_analysis_tester(
        path="i*",
        cwd="{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep)
    ) == [
               (1, -297.982681),
               (2, -299.171055),
               (3, -299.791356),
               (4, -299.845957),
               (5, -299.498399)
           ]


def test_force_analysis():
    """Tests for force_analysis"""
    assert force_analysis_tester(cwd="{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep)) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010419, -0.0, -0.0, 0.010419),
        (3, 0.00139, 0.0, 0.0, 0.00139),
        (4, -0.00179, 0.0, -0.0, 0.00179),
        (5, 0.000604, 0.0, -0.0, 0.000604)
    ]


def test_energy_diff():
    """Tests for energy_diff"""
    assert energy_diff_tester(
        path="i*",
        cwd="{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep)
    ) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]


def test_force_diff():
    """Tests for force_diff"""
    assert force_diff_tester(cwd="{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep)) == [
        [(-0.010419, 0.016003, 2, 1, 0.026422)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000604, 0.016003, 5, 1, 0.015399)]
    ]


def test_get_it():
    """Tests for get_it"""
    assert sorted(get_it_tester(
        "{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep), "continue"
    )) == [1, 2, 3, 3, 3, 4, 5]


def test_read_fdf():
    """Tests for read_fdf"""
    assert read_fdf_tester(
        "{0}{1}tests{1}assets{1}fdf{1}C-4.fdf".format(mpath, os.sep),
        ['C       0.382434   -0.000000   -0.000000', 'C       1.636103   -0.000000   -0.000000']
    ) == ("SystemName          Carbon\nSystemLabel         C\nWriteMDXmol            .true.\n" +
          "SolutionMethod     diagonal\nNumberOfSpecies     1\n%block ChemicalSpeciesLabel\n1    6    C\n" +
          "%endblock ChemicalSpeciesLabel\n\n#XC.functional GGA\n#XC.authors  PBE\n\nPAO.EnergyShift 50 meV\n\n" +
          "MeshCutoff         200.0000000     Ry\n#SpinPolarized      .true.\nMaxSCFIterations       200\n" +
          "OccupationFunction     FD\nDM.MixingWeight        0.1\nElectronicTemperature  300.0 K\n" +
          "DM.NumberPulay         5\nDM.Tolerance           0.0001   \n\nUseSaveData         .false.\n" +
          "WriteDM             .true. \n#DM.UseSaveDM        .true.\n#MD.UseSaveXV        .true.\n" +
          "MD.UseSaveCG        .false.\nWriteWaveFunctions  .true.\nWriteMullikenPop     0 \n" +
          "WriteKpoints:       .false.\nSaveRho             .false.\n\nMD.TypeOfRun         cg\n" +
          "MD.NumCGsteps        150\nMD.MaxForceTol       0.04 eV/Ang\nMD.MaxCGDispl        0.1 Bohr\n" +
          "MD.VariableCell     .false.\n\nNetCharge = 0\n\n%block kgrid_Monkhorst_Pack\n1    0    0   0.0  \n" +
          "0    1    0   0.0  \n0    0    1   0.0  \n%endblock kgrid_Monkhorst_Pack\n\n" +
          "#BandLinesScale ReciprocalLatticeVectors\n#%block BandLines\n#1   0.0 0.0 0.0 \n#101 0.0 0.0 0.5\n" +
          "#%endblock BandLines\n\n#WriteDenchar   .true.\n#%block WaveFuncKPoints\n" +
          "#  0.000  0.000  0.000 from 117 to 123\n#%endblock WaveFuncKPoints\n\n%block GeometryConstraints\n" +
          "    routine constr\n%endblock GeometryConstraints\n\nLatticeConstant  1.0     Ang\n%block LatticeVectors\n" +
          "  17.00   0.00   0.00\n  0.00   17.00   0.00\n  0.00   0.00   17.00\n%endblock LatticeVectors\n\n" +
          "NumberOfAtoms   2\n\nAtomicCoordinatesFormat  Ang\n%block AtomicCoordinatesAndAtomicSpecies\n" +
          "       0.335673   -0.000000   -0.000000  1\n       1.683000   -0.000000   -0.000000  1\n" +
          "%endblock AtomicCoordinatesAndAtomicSpecies\n",
          ["       0.382434   -0.000000   -0.000000  1", "       1.636103   -0.000000   -0.000000  1"])


def test_create_fdf():
    """Tests for create_fdf"""
    assert create_fdf_tester(
        "SystemName          Carbon\nSystemLabel         C\nWriteMDXmol            .true.\n" +
        "SolutionMethod     diagonal\nNumberOfSpecies     1\n%block ChemicalSpeciesLabel\n1    6    C\n" +
        "%endblock ChemicalSpeciesLabel\n\n#XC.functional GGA\n#XC.authors  PBE\n\nPAO.EnergyShift 50 meV\n\n" +
        "MeshCutoff         200.0000000     Ry\n#SpinPolarized      .true.\nMaxSCFIterations       200\n" +
        "OccupationFunction     FD\nDM.MixingWeight        0.1\nElectronicTemperature  300.0 K\n" +
        "DM.NumberPulay         5\nDM.Tolerance           0.0001   \n\nUseSaveData         .false.\n" +
        "WriteDM             .true. \n#DM.UseSaveDM        .true.\n#MD.UseSaveXV        .true.\n" +
        "MD.UseSaveCG        .false.\nWriteWaveFunctions  .true.\nWriteMullikenPop     0 \n" +
        "WriteKpoints:       .false.\nSaveRho             .false.\n\nMD.TypeOfRun         cg\n" +
        "MD.NumCGsteps        150\nMD.MaxForceTol       0.04 eV/Ang\nMD.MaxCGDispl        0.1 Bohr\n" +
        "MD.VariableCell     .false.\n\nNetCharge = 0\n\n%block kgrid_Monkhorst_Pack\n1    0    0   0.0  \n" +
        "0    1    0   0.0  \n0    0    1   0.0  \n%endblock kgrid_Monkhorst_Pack\n\n" +
        "#BandLinesScale ReciprocalLatticeVectors\n#%block BandLines\n#1   0.0 0.0 0.0 \n#101 0.0 0.0 0.5\n" +
        "#%endblock BandLines\n\n#WriteDenchar   .true.\n#%block WaveFuncKPoints\n" +
        "#  0.000  0.000  0.000 from 117 to 123\n#%endblock WaveFuncKPoints\n\n%block GeometryConstraints\n" +
        "    routine constr\n%endblock GeometryConstraints\n\nLatticeConstant  1.0     Ang\n%block LatticeVectors\n" +
        "  17.00   0.00   0.00\n  0.00   17.00   0.00\n  0.00   0.00   17.00\n%endblock LatticeVectors\n\n" +
        "NumberOfAtoms   2\n\nAtomicCoordinatesFormat  Ang\n%block AtomicCoordinatesAndAtomicSpecies\n" +
        "       0.335673   -0.000000   -0.000000  1\n       1.683000   -0.000000   -0.000000  1\n" +
        "%endblock AtomicCoordinatesAndAtomicSpecies\n",
        ["       0.382434   -0.000000   -0.000000  1", "       1.636103   -0.000000   -0.000000  1"],
        "{0}{1}tests{1}assets{1}temp{1}C-5.fdf".format(mpath, os.sep),
        "2"
    ) == read_file("{0}{1}tests{1}assets{1}fdf{1}C-5.fdf".format(mpath, os.sep))


def test_read_energy():
    """Tests for read_energy"""
    assert read_energy_tester(
        energies=[],
        path="{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep),
        cont="continue",
        it=[]
    ) == ([1, 2, 3, 3, 3, 4, 5], [-297.982681, -299.171055, -299.791356, -299.845957, -299.498399])


def test_print_run():
    """Tests for print_run"""
    assert print_run_tester("i1", None, None) == "Running SIESTA for i1\n"
    assert print_run_tester("i1", 4, None) == "Running SIESTA for i1 in parallel with 4 cores\n"
    assert print_run_tester("i1", None, "envir") == "Running SIESTA for i1 in conda\n"


def test_check_restart():
    """Tests for check_restart"""
    assert check_restart_tester(
        "{0}{1}tests{1}assets{1}fdf{1}H2O-1_continue.fdf".format(mpath, os.sep),
        "1",
        "H2O",
        "{0}{1}tests{1}assets{1}fdf".format(mpath, os.sep),
        "continue",
        ["DM", "XV"]
    ) == read_file("{0}{1}tests{1}assets{1}fdf{1}H2O-1_continue_2.fdf".format(mpath, os.sep))


def test_check_userbasis():
    """Tests for check_userbasis"""
    assert check_userbasis_tester("{0}{1}tests{1}assets{1}fdf{1}C-1.fdf".format(mpath, os.sep)) is False
    assert check_userbasis_tester("{0}{1}tests{1}assets{1}fdf{1}C_userbasis-1.fdf".format(mpath, os.sep)) is True


def test_copy_file():
    """Tests for copy_file"""
    assert copy_file_tester(
        "{0}{1}tests{1}assets{1}fdf{1}C-1.fdf".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}temp{1}C-1 (1).fdf".format(mpath, os.sep)
    ) == ["{0}{1}tests{1}assets{1}temp{1}C-1 (1).fdf".format(mpath, os.sep)]


def test_sort_():
    """Tests for sort_"""
    assert sort__tester(
        [
            "i1{0}log".format(os.sep),
            "i2{0}log".format(os.sep),
            "i3{0}log".format(os.sep),
            "i4{0}log".format(os.sep),
            "i2{0}continue{0}log".format(os.sep),
            "i2{0}continue_2{0}log".format(os.sep)
        ],
        "i*",
        "continue"
    ) == [
               "i1{0}log".format(os.sep),
               "i2{0}log".format(os.sep),
               "i2{0}continue{0}log".format(os.sep),
               "i2{0}continue_2{0}log".format(os.sep),
               "i3{0}log".format(os.sep),
               "i4{0}log".format(os.sep)
           ]
    assert sort__tester(
        [
            "i1{0}log".format(os.sep),
            "i11{0}log".format(os.sep),
            "i12{0}log".format(os.sep),
            "i13{0}log".format(os.sep),
            "i10{0}log".format(os.sep),
            "i2{0}log".format(os.sep),
            "i3{0}log".format(os.sep),
            "i4{0}log".format(os.sep),
            "i5{0}log".format(os.sep),
            "i6{0}log".format(os.sep),
            "i7{0}log".format(os.sep),
            "i8{0}log".format(os.sep),
            "i9{0}log".format(os.sep),
            "i11{0}continue{0}log".format(os.sep),
            "i2{0}continue{0}log".format(os.sep),
            "i2{0}continue_2{0}log".format(os.sep)],
        "i*",
        "continue"
    ) == [
               "i1{0}log".format(os.sep),
               "i2{0}log".format(os.sep),
               "i2{0}continue{0}log".format(os.sep),
               "i2{0}continue_2{0}log".format(os.sep),
               "i3{0}log".format(os.sep),
               "i4{0}log".format(os.sep),
               "i5{0}log".format(os.sep),
               "i6{0}log".format(os.sep),
               "i7{0}log".format(os.sep),
               "i8{0}log".format(os.sep),
               "i9{0}log".format(os.sep),
               "i10{0}log".format(os.sep),
               "i11{0}log".format(os.sep),
               "i11{0}continue{0}log".format(os.sep),
               "i12{0}log".format(os.sep),
               "i13{0}log".format(os.sep),
           ]
    assert sort__tester(
        [
            "i1{0}C.ANI".format(os.sep),
            "i2{0}C.ANI".format(os.sep),
            "i3{0}C.ANI".format(os.sep),
            "i4{0}C.ANI".format(os.sep),
            "i2{0}continue{0}C.ANI".format(os.sep),
            "i2{0}continue_2{0}C.ANI".format(os.sep)
        ],
        "i*",
        "continue"
    ) == [
               "i1{0}C.ANI".format(os.sep),
               "i2{0}C.ANI".format(os.sep),
               "i2{0}continue{0}C.ANI".format(os.sep),
               "i2{0}continue_2{0}C.ANI".format(os.sep),
               "i3{0}C.ANI".format(os.sep),
               "i4{0}C.ANI".format(os.sep)
           ]
    assert sort__tester(
        [
            "i1{0}C.ANI".format(os.sep),
            "i11{0}C.ANI".format(os.sep),
            "i12{0}C.ANI".format(os.sep),
            "i13{0}C.ANI".format(os.sep),
            "i10{0}C.ANI".format(os.sep),
            "i2{0}C.ANI".format(os.sep),
            "i3{0}C.ANI".format(os.sep),
            "i4{0}C.ANI".format(os.sep),
            "i5{0}C.ANI".format(os.sep),
            "i6{0}C.ANI".format(os.sep),
            "i7{0}C.ANI".format(os.sep),
            "i8{0}C.ANI".format(os.sep),
            "i9{0}C.ANI".format(os.sep),
            "i11{0}continue{0}C.ANI".format(os.sep),
            "i2{0}continue{0}C.ANI".format(os.sep),
            "i2{0}continue_2{0}C.ANI".format(os.sep)
        ],
        "i*",
        "continue"
    ) == [
               "i1{0}C.ANI".format(os.sep),
               "i2{0}C.ANI".format(os.sep),
               "i2{0}continue{0}C.ANI".format(os.sep),
               "i2{0}continue_2{0}C.ANI".format(os.sep),
               "i3{0}C.ANI".format(os.sep),
               "i4{0}C.ANI".format(os.sep),
               "i5{0}C.ANI".format(os.sep),
               "i6{0}C.ANI".format(os.sep),
               "i7{0}C.ANI".format(os.sep),
               "i8{0}C.ANI".format(os.sep),
               "i9{0}C.ANI".format(os.sep),
               "i10{0}C.ANI".format(os.sep),
               "i11{0}C.ANI".format(os.sep),
               "i11{0}continue{0}C.ANI".format(os.sep),
               "i12{0}C.ANI".format(os.sep),
               "i13{0}C.ANI".format(os.sep)
           ]
    assert sort__tester(
        [
            "i1",
            "i2",
            "i3",
            "i4",
            "i2{0}continue".format(os.sep),
            "i2{0}continue_2".format(os.sep)
        ],
        "i*",
        "continue"
    ) == [
               "i1",
               "i2",
               "i2{0}continue".format(os.sep),
               "i2{0}continue_2".format(os.sep),
               "i3",
               "i4"
           ]
    assert sort__tester(
        [
            "i1",
            "i11",
            "i12",
            "i13",
            "i10",
            "i2",
            "i3",
            "i4",
            "i5",
            "i6",
            "i7",
            "i8",
            "i9",
            "i11{0}continue".format(os.sep),
            "i2{0}continue".format(os.sep),
            "i2{0}continue_2".format(os.sep)],
        "i*",
        "continue"
    ) == [
               "i1",
               "i2",
               "i2{0}continue".format(os.sep),
               "i2{0}continue_2".format(os.sep),
               "i3",
               "i4",
               "i5",
               "i6",
               "i7",
               "i8",
               "i9",
               "i10",
               "i11",
               "i11{0}continue".format(os.sep),
               "i12",
               "i13"
           ]


def test_remove_nones():
    """Tests for remove_nones"""
    assert remove_nones_tester(
        [
            "{0}home{0}user{0}compound{0}i1{0}log".format(os.sep),
            "{0}home{0}user{0}compound{0}i2{0}log".format(os.sep),
            "{0}home{0}user{0}compound{0}i2{0}continue{0}log".format(os.sep),
            "{0}home{0}user{0}compound{0}i2{0}continue_2{0}log".format(os.sep),
            "{0}home{0}user{0}compound{0}i3{0}log".format(os.sep),
            "{0}home{0}user{0}compound{0}i4{0}log".format(os.sep)
        ],
        "i*",
        "{0}home{0}user{0}compound".format(os.sep),
        "continue",
        "log"
    ) == [
               "{0}home{0}user{0}compound{0}i1{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i2{0}continue_2{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i3{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i4{0}log".format(os.sep)
           ]
    assert remove_nones_tester([
        "{0}home{0}user{0}compound{0}i1{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i2{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i2{0}continue{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i2{0}continue_2{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i3{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i4{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i5{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i6{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i7{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i8{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i9{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i10{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i11{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i11{0}continue{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i12{0}log".format(os.sep),
        "{0}home{0}user{0}compound{0}i13{0}log".format(os.sep)
    ],
        "i*",
        "{0}home{0}user{0}compound".format(os.sep),
        "continue",
        "log"
    ) == [
               "{0}home{0}user{0}compound{0}i1{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i2{0}continue_2{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i3{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i4{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i5{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i6{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i7{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i8{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i9{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i10{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i11{0}continue{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i12{0}log".format(os.sep),
               "{0}home{0}user{0}compound{0}i13{0}log".format(os.sep)
           ]


def test_carbon_uninterrupted_project():
    """Run tests based on Carbon_uninterrupted run"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    initialise_fake_project()
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("ANI")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    assert copy_files_tester(["psf"], "C", ".", "i1") == ["i1{0}C.psf".format(os.sep)]
    assert xyz_to_fdf_tester("C.xyz", "C.fdf", "i1{0}C.fdf".format(os.sep)) == read_file(
        "{0}{1}tests{1}assets{1}runs{1}{2}{1}i1{1}C.fdf".format(mpath, os.sep, get_fake_project())
    )
    assert "All iterations are completed" in run_tester("C")
    assert energy_analysis_tester(cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010419, -0.0, -0.0, 0.010419),
        (3, 0.00139, 0.0, 0.0, 0.00139),
        (4, -0.00179, 0.0, -0.0, 0.00179),
        (5, 0.000604, 0.0, -0.0, 0.000604)
    ]
    assert energy_diff_tester(cwd=settings.get_cwd()) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010419, 0.016003, 2, 1, 0.026422)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000604, 0.016003, 5, 1, 0.015399)]
    ]


def test_carbon_uninterrupted_project_run_next():
    """Run tests based on Carbon_uninterrupted run run_next function"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("ANI")
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in run_next_tester("2", "C")
    assert energy_analysis_tester(path="i*", cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010419, -0.0, -0.0, 0.010419),
        (3, 0.00139, 0.0, 0.0, 0.00139),
        (4, -0.00179, 0.0, -0.0, 0.00179),
        (5, 0.000604, 0.0, -0.0, 0.000604)
    ]
    assert energy_diff_tester(path="i*", cwd=settings.get_cwd()) == [
        (
            -299.845957,
            -297.982681,
            4,
            1,
            1.8632759999999848
        )
    ]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010419, 0.016003, 2, 1, 0.026422)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000604, 0.016003, 5, 1, 0.015399)]
    ]


def test_carbon_uninterrupted_project_single_run():
    """Run tests based on Carbon_uninterrupted run single_run function"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("ANI")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in single_run_tester("3", "C")


def test_carbon_project_run_interrupted():
    """Run tests based on Carbon run run_interrupted function"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_cont("continue")
    settings.set_contfrom("ANI")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in run_interrupted_tester("3", "C")
    assert energy_analysis_tester(path="i*", cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010419, -0.0, -0.0, 0.010419),
        (3, 0.00139, 0.0, 0.0, 0.00139),
        (4, -0.00179, 0.0, -0.0, 0.00179),
        (5, 0.000604, 0.0, -0.0, 0.000604)
    ]
    assert energy_diff_tester(path="i*", cwd=settings.get_cwd()) == [
        (
            -299.845957,
            -297.982681,
            4,
            1,
            1.8632759999999848
        )
    ]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010419, 0.016003, 2, 1, 0.026422)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000604, 0.016003, 5, 1, 0.015399)]
    ]


def test_carbon_project_single_run_interrupted():
    """Run tests based on Carbon run single_run_interrupted function"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("ANI")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in single_run_interrupted_tester("3", "C")


def test_carbon_xv_uninterrupted_project():
    """Run tests based on Carbon_XV_uninterrupted run"""
    fake_command()
    set_fake_project("Carbon_XV_uninterrupted")
    initialise_fake_project()
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("XV")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    assert copy_files_tester(["psf"], "C", ".", "i1") == ["i1{0}C.psf".format(os.sep)]
    assert xyz_to_fdf_tester("C.xyz", "C.fdf", "i1{0}C.fdf".format(os.sep)) == read_file(
        "{0}{1}tests{1}assets{1}runs{1}{2}{1}i1{1}C.fdf".format(mpath, os.sep, get_fake_project())
    )
    assert "All iterations are completed" in run_tester("C")
    assert energy_analysis_tester(cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010419, -0.0, -0.0, 0.010419),
        (3, 0.00139, 0.0, 0.0, 0.00139),
        (4, -0.00179, 0.0, -0.0, 0.00179),
        (5, 0.000604, 0.0, -0.0, 0.000604)
    ]
    assert energy_diff_tester(cwd=settings.get_cwd()) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010419, 0.016003, 2, 1, 0.026422)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000604, 0.016003, 5, 1, 0.015399)]
    ]


def test_carbon_xv_uninterrupted_project_run_next():
    """Run tests based on Carbon_XV_uninterrupted run run_next function"""
    fake_command()
    set_fake_project("Carbon_XV_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("XV")
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in run_next_tester("2", "C")
    assert energy_analysis_tester(path="i*", cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010419, -0.0, -0.0, 0.010419),
        (3, 0.00139, 0.0, 0.0, 0.00139),
        (4, -0.00179, 0.0, -0.0, 0.00179),
        (5, 0.000604, 0.0, -0.0, 0.000604)
    ]
    assert energy_diff_tester(path="i*", cwd=settings.get_cwd()) == [
        (
            -299.845957,
            -297.982681,
            4,
            1,
            1.8632759999999848
        )
    ]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010419, 0.016003, 2, 1, 0.026422)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000604, 0.016003, 5, 1, 0.015399)]
    ]


def test_carbon_xv_uninterrupted_project_single_run():
    """Run tests based on Carbon_XV_uninterrupted run single_run function"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("XV")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in single_run_tester("3", "C")


def test_carbon_xv_project_run_interrupted():
    """Run tests based on Carbon_XV run run_interrupted function"""
    fake_command()
    set_fake_project("Carbon_XV")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_cont("continue")
    settings.set_contfrom("XV")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in run_interrupted_tester("3", "C")
    assert energy_analysis_tester(path="i*", cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791357),
        (4, -299.845956),
        (5, -299.498399)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010418, -0.0, -0.0, 0.010418),
        (3, 0.001391, -0.0, -0.0, 0.001391),
        (4, -0.001789, -0.0, -0.0, 0.001789),
        (5, 0.000606, 0.0, -0.0, 0.000606)
    ]
    assert energy_diff_tester(path="i*", cwd=settings.get_cwd()) == [
        (
            -299.845956,
            -297.982681,
            4,
            1,
            1.8632749999999874
        )
    ]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010418, 0.016003, 2, 1, 0.026421)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (-0.0, -0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (-0.0, -0.0, 3, 3, 0.0),
         (-0.0, -0.0, 4, 4, 0.0),
         (-0.0, -0.0, 5, 5, 0.0)],
        [(0.000606, 0.016003, 5, 1, 0.015397)]
    ]


def test_carbon_xv_project_single_run_interrupted():
    """Run tests based on Carbon_XV run single_run_interrupted function"""
    fake_command()
    set_fake_project("Carbon_XV")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("XV")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in single_run_interrupted_tester("3", "C")


def test_carbon_log_uninterrupted_project():
    """Run tests based on Carbon_log_uninterrupted run"""
    fake_command()
    set_fake_project("Carbon_log_uninterrupted")
    initialise_fake_project()
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("log")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    assert copy_files_tester(["psf"], "C", ".", "i1") == ["i1{0}C.psf".format(os.sep)]
    assert xyz_to_fdf_tester("C.xyz", "C.fdf", "i1{0}C.fdf".format(os.sep)) == read_file(
        "{0}{1}tests{1}assets{1}runs{1}{2}{1}i1{1}C.fdf".format(mpath, os.sep, get_fake_project())
    )
    assert "All iterations are completed" in run_tester("C")
    assert energy_analysis_tester(cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171087),
        (3, -299.791357),
        (4, -299.845956),
        (5, -299.498398)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010418, -0.0, 0.0, 0.010418),
        (3, 0.001391, -0.0, 0.0, 0.001391),
        (4, -0.001789, 0.0, 0.0, 0.001789),
        (5, 0.000605, 0.0, 0.0, 0.000605)
    ]
    assert energy_diff_tester(cwd=settings.get_cwd()) == [(-299.845956, -297.982681, 4, 1, 1.8632749999999874)]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010418, 0.016003, 2, 1, 0.026421)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (-0.0, -0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (0.0, 0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.000605, 0.016003, 5, 1, 0.015398)]
    ]


def test_carbon_log_uninterrupted_project_run_next():
    """Run tests based on Carbon_log_uninterrupted run run_next function"""
    fake_command()
    set_fake_project("Carbon_log_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("log")
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in run_next_tester("2", "C")
    assert energy_analysis_tester(cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171087),
        (3, -299.791357),
        (4, -299.845956),
        (5, -299.498398)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010418, -0.0, 0.0, 0.010418),
        (3, 0.001391, -0.0, 0.0, 0.001391),
        (4, -0.001789, 0.0, 0.0, 0.001789),
        (5, 0.000605, 0.0, 0.0, 0.000605)
    ]
    assert energy_diff_tester(cwd=settings.get_cwd()) == [(-299.845956, -297.982681, 4, 1, 1.8632749999999874)]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010418, 0.016003, 2, 1, 0.026421)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (-0.0, -0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (0.0, 0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.000605, 0.016003, 5, 1, 0.015398)]
    ]


def test_carbon_log_uninterrupted_project_single_run():
    """Run tests based on Carbon_log_uninterrupted run single_run function"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("log")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in single_run_tester("3", "C")


def test_carbon_log_project_run_interrupted():
    """Run tests based on Carbon_log run run_interrupted function"""
    fake_command()
    set_fake_project("Carbon_log")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_cont("continue")
    settings.set_contfrom("log")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in run_interrupted_tester("3", "C")
    assert energy_analysis_tester(cwd=settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171087),
        (3, -299.791357),
        (4, -299.845956),
        (5, -299.498398)
    ]
    assert force_analysis_tester(cwd=settings.get_cwd()) == [
        (1, 0.016003, 0.0, 0.0, 0.016003),
        (2, -0.010418, -0.0, 0.0, 0.010418),
        (3, 0.001391, -0.0, 0.0, 0.001391),
        (4, -0.001789, 0.0, 0.0, 0.001789),
        (5, 0.000605, 0.0, 0.0, 0.000605)
    ]
    assert energy_diff_tester(cwd=settings.get_cwd()) == [(-299.845956, -297.982681, 4, 1, 1.8632749999999874)]
    assert force_diff_tester(cwd=settings.get_cwd()) == [
        [(-0.010418, 0.016003, 2, 1, 0.026421)],
        [(0.0, 0.0, 1, 1, 0.0),
         (-0.0, -0.0, 2, 2, 0.0),
         (-0.0, -0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.0, 0.0, 1, 1, 0.0),
         (0.0, 0.0, 2, 2, 0.0),
         (0.0, 0.0, 3, 3, 0.0),
         (0.0, 0.0, 4, 4, 0.0),
         (0.0, 0.0, 5, 5, 0.0)],
        [(0.000605, 0.016003, 5, 1, 0.015398)]
    ]


def test_carbon_log_project_single_run_interrupted():
    """Run tests based on Carbon_log run single_run_interrupted function"""
    fake_command()
    set_fake_project("Carbon_log")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    settings.set_contfrom("log")
    assert make_directories_tester(5) == [
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i1".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i2".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i3".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i4".format(mpath, os.sep, get_fake_project()),
        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i5".format(mpath, os.sep, get_fake_project())
    ]
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in single_run_interrupted_tester("3", "C")


def test_main():
    """Tests for __main__.py"""
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " ani_to_fdf" +
        " {0}{1}tests{1}assets{1}ANI{1}C-4.ANI".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}fdf{1}C-0.fdf".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}temp{1}C-5.fdf".format(mpath, os.sep)
    )
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xyz_to_fdf" +
        " {0}{1}tests{1}assets{1}xyz{1}C.xyz".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}fdf{1}C-0.fdf".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}temp{1}C-1.fdf".format(mpath, os.sep)
    )
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xv_to_fdf" +
        " {0}{1}tests{1}assets{1}XV{1}C-XV-1.XV".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}fdf{1}C-XV-1.fdf".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}temp{1}C-XV-2.fdf".format(mpath, os.sep)
    )
    if os.path.exists("{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep)):
        shutil.rmtree("{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep))
    shutil.copytree(
        "{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep),
        "{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep)
    )
    settings.set_cwd("{0}{1}tests{1}assets{1}temp{1}Carbon".format(mpath, os.sep))
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C path=i*")
    clear_temp()
    set_fake_project("Carbon")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    import glob
    assert len(main_tester(
        "SIESTAstepper" +
        " copy_files" +
        " C" +
        " {0}{1}tests{1}assets{1}runs{1}Carbon{1}i1".format(mpath, os.sep) +
        " {0}{1}tests{1}assets{1}temp{1}Carbon{1}i2".format(mpath, os.sep) +
        " psf" +
        " XV" +
        " DM"
    ).split("successfully")) == 4
    settings.set_cwd("{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep))
    os.chdir(settings.get_cwd())
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total cont=continue path=i* noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert (
        (expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr in [
            "0.016003",
            "0.010419",
            "0.00139",
            "0.00179",
            "0.000604"
        ]
    )
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_uninterrupted_project():
    """Run tests based on Carbon_uninterrupted run with __main__.py"""
    set_fake_project("Carbon_uninterrupted")
    initialise_fake_project()
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    assert len(main_tester(
        "SIESTAstepper" +
        " copy_files" +
        " C" +
        " ." +
        " i1" +
        " psf"
    ).split("successfully")) == 2
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xyz_to_fdf" +
        " C.xyz" +
        " C.fdf" +
        " i1{0}C.fdf".format(os.sep)
    )
    assert "All iterations are completed" in main_tester(
        "SIESTAstepper run log C mpirun=4 siesta=siesta_p contfrom=ANI"
    )
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_uninterrupted_project_run_next():
    """Run tests based on Carbon_uninterrupted run run_next function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 is created",
        "i2 is created",
        "i3 is created",
        "i4 is created",
        "i5 is created"
    ])
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in main_tester("SIESTAstepper run_next log 2 C contfrom=ANI")
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_uninterrupted_project_single_run():
    """Run tests based on Carbon_uninterrupted run single_run function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 is created",
        "i2 is created",
        "i3 is created",
        "i4 is created",
        "i5 is created"
    ])
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run log 2 C contfrom=ANI")


def test_main_carbon_project_run_interrupted():
    """Run tests based on Carbon run run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in main_tester(
        "SIESTAstepper run_interrupted log 3 C cont=continue contfrom=ANI"
    )
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total cont=continue noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total cont=continue")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_project_single_run_interrupted():
    """Run tests based on Carbon run single_run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run_interrupted log 3 C contfrom=ANI")


def test_main_carbon_xv_uninterrupted_project():
    """Run tests based on Carbon_XV_uninterrupted run with __main__.py"""
    set_fake_project("Carbon_XV_uninterrupted")
    initialise_fake_project()
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    assert len(main_tester(
        "SIESTAstepper" +
        " copy_files" +
        " C" +
        " ." +
        " i1" +
        " psf"
    ).split("successfully")) == 2
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xyz_to_fdf" +
        " C.xyz" +
        " C.fdf" +
        " i1{0}C.fdf".format(os.sep)
    )
    assert "All iterations are completed" in main_tester(
        "SIESTAstepper run log C mpirun=4 siesta=siesta_p contfrom=XV"
    )
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_xv_uninterrupted_project_run_next():
    """Run tests based on Carbon_XV_uninterrupted run run_next function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_XV_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 is created",
        "i2 is created",
        "i3 is created",
        "i4 is created",
        "i5 is created"
    ])
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in main_tester("SIESTAstepper run_next log 2 C contfrom=XV")
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_xv_uninterrupted_project_single_run():
    """Run tests based on Carbon_XV_uninterrupted run single_run function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 is created",
        "i2 is created",
        "i3 is created",
        "i4 is created",
        "i5 is created"
    ])
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run log 2 C contfrom=XV")


def test_main_carbon_xv_project_run_interrupted():
    """Run tests based on Carbon_XV run run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_XV")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in main_tester(
        "SIESTAstepper run_interrupted log 3 C cont=continue contfrom=XV"
    )
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total cont=continue noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total cont=continue")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_xv_project_single_run_interrupted():
    """Run tests based on Carbon_XV run single_run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_XV")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run_interrupted log 3 C contfrom=XV")


def test_main_carbon_log_uninterrupted_project():
    """Run tests based on Carbon_log_uninterrupted run with __main__.py"""
    set_fake_project("Carbon_log_uninterrupted")
    initialise_fake_project()
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    assert len(main_tester(
        "SIESTAstepper" +
        " copy_files" +
        " C" +
        " ." +
        " i1" +
        " psf"
    ).split("successfully")) == 2
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xyz_to_fdf" +
        " C.xyz" +
        " C.fdf" +
        " i1{0}C.fdf".format(os.sep)
    )
    assert "All iterations are completed" in main_tester(
        "SIESTAstepper run log C mpirun=4 siesta=siesta_p contfrom=log"
    )
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_log_uninterrupted_project_run_next():
    """Run tests based on Carbon_log_uninterrupted run run_next function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_log_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 is created",
        "i2 is created",
        "i3 is created",
        "i4 is created",
        "i5 is created"
    ])
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in main_tester("SIESTAstepper run_next log 2 C contfrom=log")
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_log_uninterrupted_project_single_run():
    """Run tests based on Carbon_log_uninterrupted run single_run function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 is created",
        "i2 is created",
        "i3 is created",
        "i4 is created",
        "i5 is created"
    ])
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run log 2 C contfrom=log")


def test_main_carbon_log_project_run_interrupted():
    """Run tests based on Carbon_log run run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_log")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        "{0}{1}i1".format(os.getcwd(), os.sep),
        "{0}{1}i2".format(os.getcwd(), os.sep),
        "{0}{1}i3".format(os.getcwd(), os.sep),
        "{0}{1}i4".format(os.getcwd(), os.sep),
        "{0}{1}i5".format(os.getcwd(), os.sep)
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in main_tester(
        "SIESTAstepper run_interrupted log 3 C cont=continue contfrom=log"
    )
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    assert ((expr in main_tester("SIESTAstepper energy_analysis log total cont=continue noplot")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper force_analysis log atomic Tot cont=continue path=i* noplot")) for expr
            in [
                "0.016003",
                "0.010419",
                "0.00139",
                "0.00179",
                "0.000604"
            ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log total cont=continue")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])
    assert ((expr in main_tester("SIESTAstepper force_diff log atomic Tot")) for expr in [
        "[-0.010419]",
        "[0.016003]",
        "[0.026422]",
        "[ 0. -0.  0.  0.  0.]",
        "[ 0. -0.  0.  0.  0.]",
        "[0. 0. 0. 0. 0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[ 0. -0.  0. -0. -0.]",
        "[0. 0. 0. 0. 0.]",
        "[0.000604]",
        "[0.015399]"
    ])


def test_main_carbon_log_project_single_run_interrupted():
    """Run tests based on Carbon_log run single_run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_log")
    os.chdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, get_fake_project()))
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run_interrupted log 3 C contfrom=log")


class TestErrors(unittest.TestCase):
    """Unit testing of errors"""

    def __init__(self, methodName='runTest'):
        """Initialise"""
        self._testMethodName = methodName

    def test_main(self):
        """Error tests for __main__.py"""
        with self.assertRaises(AttributeError):
            main_tester("SIESTAstepper Foo")

    def test_pair_correlation_function(self):
        """Error tests for pair_correlation_function"""
        with self.assertRaises(RuntimeError):
            pair_correlation_function_tester(
                label="C",
                cwd="{0}{1}tests{1}assets{1}runs{1}Carbon".format(mpath, os.sep)
            )

    # def test_get_it(self):
    #     """Error tests for get_it"""
    #     with self.assertRaises(AttributeError):
    #         get_it_tester("Foo", "Bar")

    def test_copy_file(self):
        """Error tests for copy_file"""
        # with self.assertRaises(shutil.SameFileError):
        #    copy_file_tester(
        #        "{0}{1}tests{1}assets{1}runs{1}{2}{1}i1{1}C.fdf".format(mpath, os.sep, get_fake_project()),
        #        "{0}{1}tests{1}assets{1}runs{1}{2}{1}i1{1}C.fdf".format(mpath, os.sep, get_fake_project())
        #    )
        with self.assertRaises(FileNotFoundError):
            copy_file_tester("Foo", "Bar")
