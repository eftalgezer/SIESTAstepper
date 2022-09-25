"""
Unit tests for the SIESTAstepper library.
"""
from __future__ import absolute_import
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
    merge_ani_tester,
    run_tester,
    run_interrupted_tester,
    single_run_interrupted_tester,
    make_directories_tester,
    copy_files_tester,
    analysis_tester,
    energy_diff_tester,
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

mpath = mfile.replace("/SIESTAstepper/__init__.py", "")


def test_ani_to_fdf():
    """Tests for ani_to_fdf"""
    assert ani_to_fdf_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-4.ANI",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-5.fdf"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-5.fdf")


def test_xyz_to_fdf():
    """Tests for xyz_to_fdf"""
    assert xyz_to_fdf_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}xyz{os.sep}C.xyz",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-1.fdf"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-1.fdf")


def test_merge_ani():
    """Tests for merge_ani"""
    assert merge_ani_tester(label="C", folder="Carbon") == read_file(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI"
    )


def test_make_directories():
    """Tests for make_directories"""
    if not os.path.isdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon"):
        os.mkdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon")
    assert make_directories_tester(5) == [
        f"{os.getcwd()}{os.sep}i1",
        f"{os.getcwd()}{os.sep}i2",
        f"{os.getcwd()}{os.sep}i3",
        f"{os.getcwd()}{os.sep}i4",
        f"{os.getcwd()}{os.sep}i5"
    ]


def test_copy_files():
    """Tests for copy_files"""
    assert copy_files_tester(
        ["psf", "DM", "XV"], "C",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon{os.sep}i2"
    ) == [
               f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon{os.sep}i2{os.sep}C.psf",
               f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon{os.sep}i2{os.sep}C.DM",
               f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon{os.sep}i2{os.sep}C.XV"
           ]


def test_analysis():
    """Tests for analysis"""
    assert analysis_tester(
        "i*",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon"
    ) == [
               (1, -297.982681),
               (2, -299.171055),
               (3, -299.791356),
               (4, -299.845957),
               (5, -299.498399)
           ]


def test_energy_diff():
    """Tests for energy_diff"""
    assert energy_diff_tester(
        "i*",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon"
    ) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]


def test_get_it():
    """Tests for get_it"""
    assert sorted(get_it_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon", "continue"
    )) == [1, 2, 3, 3, 3, 4, 5]


def test_read_fdf():
    """Tests for read_fdf"""
    assert read_fdf_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-4.fdf",
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
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-5.fdf",
        "2"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-5.fdf")


def test_read_energy():
    """Tests for read_energy"""
    assert read_energy_tester(
        energies=[],
        path=f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon",
        cont="continue",
        it=[]
    ) == ([1, 2, 3, 3, 3, 4, 5], [-297.982681, -299.171055, -299.791356, -299.845957, -299.498399])


def test_print_run():
    """Tests for print_run"""
    assert print_run_tester("i1", None, None) == "Running SIESTA for i1\n"


def test_check_restart():
    """Tests for check_restart"""
    assert check_restart_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}H2O-1_continue.fdf",
        "1",
        "H2O",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf",
        "continue",
        ["DM", "XV"]
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}H2O-1_continue_2.fdf")


def test_check_userbasis():
    """Tests for check_userbasis"""
    assert check_userbasis_tester(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-1.fdf") is False
    assert check_userbasis_tester(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C_userbasis-1.fdf") is True


def test_copy_file():
    """Tests for copy_file"""
    assert copy_file_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-1.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-1 (1).fdf"
    ) == [f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-1 (1).fdf"]


def test_sort_():
    """Tests for sort_"""
    assert sort__tester(
        [
            f"i1{os.sep}log",
            f"i2{os.sep}log",
            f"i3{os.sep}log",
            f"i4{os.sep}log",
            f"i2{os.sep}continue{os.sep}log",
            f"i2{os.sep}continue_2{os.sep}log"
        ],
        "i*",
        "continue"
    ) == [
               f"i1{os.sep}log",
               f"i2{os.sep}log",
               f"i2{os.sep}continue{os.sep}log",
               f"i2{os.sep}continue_2{os.sep}log",
               f"i3{os.sep}log",
               f"i4{os.sep}log"
           ]
    assert sort__tester(
        [
            f"i1{os.sep}log",
            f"i11{os.sep}log",
            f"i12{os.sep}log",
            f"i13{os.sep}log",
            f"i10{os.sep}log",
            f"i2{os.sep}log",
            f"i3{os.sep}log",
            f"i4{os.sep}log",
            f"i5{os.sep}log",
            f"i6{os.sep}log",
            f"i7{os.sep}log",
            f"i8{os.sep}log",
            f"i9{os.sep}log",
            f"i11{os.sep}continue{os.sep}log",
            f"i2{os.sep}continue{os.sep}log",
            f"i2{os.sep}continue_2{os.sep}log"],
        "i*",
        "continue"
    ) == [
               f"i1{os.sep}log",
               f"i2{os.sep}log",
               f"i2{os.sep}continue{os.sep}log",
               f"i2{os.sep}continue_2{os.sep}log",
               f"i3{os.sep}log",
               f"i4{os.sep}log",
               f"i5{os.sep}log",
               f"i6{os.sep}log",
               f"i7{os.sep}log",
               f"i8{os.sep}log",
               f"i9{os.sep}log",
               f"i10{os.sep}log",
               f"i11{os.sep}log",
               f"i11{os.sep}continue{os.sep}log",
               f"i12{os.sep}log",
               f"i13{os.sep}log",
           ]
    assert sort__tester(
        [
            f"i1{os.sep}C.ANI",
            f"i2{os.sep}C.ANI",
            f"i3{os.sep}C.ANI",
            f"i4{os.sep}C.ANI",
            f"i2{os.sep}continue{os.sep}C.ANI",
            f"i2{os.sep}continue_2{os.sep}C.ANI"],
        "i*",
        "continue"
    ) == [
               f"i1{os.sep}C.ANI",
               f"i2{os.sep}C.ANI",
               f"i2{os.sep}continue{os.sep}C.ANI",
               f"i2{os.sep}continue_2{os.sep}C.ANI",
               f"i3{os.sep}C.ANI",
               f"i4{os.sep}C.ANI"
           ]
    assert sort__tester(
        [
            f"i1{os.sep}C.ANI",
            f"i11{os.sep}C.ANI",
            f"i12{os.sep}C.ANI",
            f"i13{os.sep}C.ANI",
            f"i10{os.sep}C.ANI",
            f"i2{os.sep}C.ANI",
            f"i3{os.sep}C.ANI",
            f"i4{os.sep}C.ANI",
            f"i5{os.sep}C.ANI",
            f"i6{os.sep}C.ANI",
            f"i7{os.sep}C.ANI",
            f"i8{os.sep}C.ANI",
            f"i9{os.sep}C.ANI",
            f"i11{os.sep}continue{os.sep}C.ANI",
            f"i2{os.sep}continue{os.sep}C.ANI",
            f"i2{os.sep}continue_2{os.sep}C.ANI"],
        "i*",
        "continue"
    ) == [
               f"i1{os.sep}C.ANI",
               f"i2{os.sep}C.ANI",
               f"i2{os.sep}continue{os.sep}C.ANI",
               f"i2{os.sep}continue_2{os.sep}C.ANI",
               f"i3{os.sep}C.ANI",
               f"i4{os.sep}C.ANI",
               f"i5{os.sep}C.ANI",
               f"i6{os.sep}C.ANI",
               f"i7{os.sep}C.ANI",
               f"i8{os.sep}C.ANI",
               f"i9{os.sep}C.ANI",
               f"i10{os.sep}C.ANI",
               f"i11{os.sep}C.ANI",
               f"i11{os.sep}continue{os.sep}C.ANI",
               f"i12{os.sep}C.ANI",
               f"i13{os.sep}C.ANI"
           ]
    assert sort__tester(
        [
            "i1",
            "i2",
            "i3",
            "i4",
            f"i2{os.sep}continue",
            f"i2{os.sep}continue_2"],
        "i*",
        "continue"
    ) == [
               "i1",
               "i2",
               f"i2{os.sep}continue",
               f"i2{os.sep}continue_2",
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
            f"i11{os.sep}continue",
            f"i2{os.sep}continue",
            f"i2{os.sep}continue_2"],
        "i*",
        "continue"
    ) == [
               "i1",
               "i2",
               f"i2{os.sep}continue",
               f"i2{os.sep}continue_2",
               "i3",
               "i4",
               "i5",
               "i6",
               "i7",
               "i8",
               "i9",
               "i10",
               "i11",
               f"i11{os.sep}continue",
               "i12",
               "i13"
           ]


def test_remove_nones():
    """Tests for remove_nones"""
    assert remove_nones_tester(
        [
            f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i1{os.sep}log",
            f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}log",
            f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}continue{os.sep}log",
            f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}continue_2{os.sep}log",
            f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i3{os.sep}log",
            f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i4{os.sep}log"
        ],
        "i*",
        f"{os.sep}home{os.sep}user{os.sep}compound",
        "continue",
        "log"
    ) == [
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i1{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}continue_2{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i3{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i4{os.sep}log"
           ]
    assert remove_nones_tester([
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i1{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}continue{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}continue_2{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i3{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i4{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i5{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i6{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i7{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i8{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i9{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i10{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i11{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i11{os.sep}continue{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i12{os.sep}log",
        f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i13{os.sep}log"
    ],
        "i*",
        f"{os.sep}home{os.sep}user{os.sep}compound",
        "continue",
        "log"
    ) == [
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i1{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i2{os.sep}continue_2{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i3{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i4{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i5{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i6{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i7{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i8{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i9{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i10{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i11{os.sep}continue{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i12{os.sep}log",
               f"{os.sep}home{os.sep}user{os.sep}compound{os.sep}i13{os.sep}log"
           ]


def test_carbon_uninterrupted_project():
    """Run tests based on Carbon_uninterrupted run"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    initialise_fake_project()
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i2",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i3",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i4",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i5"
    ]
    assert copy_files_tester(["psf"], "C", ".", "i1") == [f"i1{os.sep}C.psf"]
    assert xyz_to_fdf_tester("C.xyz", "C.fdf", f"i1{os.sep}C.fdf") == read_file(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}{get_fake_project()}{os.sep}i1{os.sep}C.fdf"
    )
    assert "All iterations are completed" in run_tester("C")
    assert analysis_tester("i*", settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert energy_diff_tester("i*", settings.get_cwd()) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]


def test_carbon_uninterrupted_project_run_next():
    """Run tests based on Carbon_uninterrupted run run_next function"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    assert make_directories_tester(5) == [
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i2",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i3",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i4",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i5"
    ]
    settings.set_cwd(os.getcwd())
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in run_next_tester("2", "C")
    assert analysis_tester("i*", settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert energy_diff_tester("i*", settings.get_cwd()) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]


def test_carbon_uninterrupted_project_single_run():
    """Run tests based on Carbon_uninterrupted run single_run function"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i2",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i3",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i4",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i5"
    ]
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in single_run_tester("3", "C")


def test_carbon_project_run_interrupted():
    """Run tests based on Carbon_uninterrupted run run_interrupted function"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    settings.set_cont("continue")
    assert make_directories_tester(5) == [
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i2",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i3",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i4",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i5"
    ]
    initialise_fake_project("run_interrupted 3 2")
    assert "All iterations are completed" in run_interrupted_tester("3", "C")
    assert analysis_tester("i*", settings.get_cwd()) == [
        (1, -297.982681),
        (2, -299.171055),
        (3, -299.791356),
        (4, -299.845957),
        (5, -299.498399)
    ]
    assert energy_diff_tester("i*", settings.get_cwd()) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]


def test_carbon_project_single_run_interrupted():
    """Run tests based on Carbon_uninterrupted run single_run_interrupted function"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert make_directories_tester(5) == [
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i2",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i3",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i4",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}{os.sep}i5"
    ]
    initialise_fake_project("single_run_interrupted 3 2")
    assert "Job completed\n" in single_run_interrupted_tester("3", "C")


def test_main():
    """Tests for __main__.py"""
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " ani_to_fdf" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-4.ANI" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-5.fdf"
    )
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xyz_to_fdf" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}xyz{os.sep}C.xyz" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-1.fdf"
    )
    if os.path.exists(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon"):
        shutil.rmtree(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon")
    shutil.copytree(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon"
    )
    settings.set_cwd(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon")
    assert "All ANI files are merged" in main_tester("SIESTAstepper merge_ani C")
    clear_temp()
    if not os.path.isdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon"):
        os.mkdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon")
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    print("***", glob.glob("i*"))
    assert len((main_tester(
        "SIESTAstepper" +
        " copy_files" +
        " C" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon{os.sep}i1" +
        f" {mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}Carbon{os.sep}i2" +
        " psf" +
        " XV" +
        " DM"
    ) + "*").split("successfully")) == 3
    settings.set_cwd(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}Carbon")
    os.chdir(settings.get_cwd())
    assert ((expr in main_tester("SIESTAstepper analysis log")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])


def main_carbon_uninterrupted_project():
    """Run tests based on Carbon_uninterrupted run with __main__.py"""
    set_fake_project("Carbon_uninterrupted")
    initialise_fake_project()
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    assert len((main_tester(
        "SIESTAstepper" +
        " copy_files" +
        " C" +
        " ." +
        " i1" +
        " psf"
    ) + "*").split("successfully")) == 1
    assert "is created" in main_tester(
        "SIESTAstepper" +
        " xyz_to_fdf" +
        " C.xyz" +
        " C.fdf" +
        f" i1{os.sep}C.fdf"
    )
    assert "All iterations are completed" in main_tester("SIESTAstepper run log C")
    assert ((expr in main_tester("SIESTAstepper analysis log")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])


def test_main_carbon_uninterrupted_project_run_next():
    """Run tests based on Carbon_uninterrupted run run_next function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    initialise_fake_project("run_next 2")
    assert "All iterations are completed" in main_tester("SIESTAstepper run_next log 2 C")
    assert ((expr in main_tester("SIESTAstepper analysis log")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])


def test_main_carbon_uninterrupted_project_single_run():
    """Run tests based on Carbon_uninterrupted run single_run function with __main__.py"""
    fake_command()
    set_fake_project("Carbon_uninterrupted")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    initialise_fake_project("single_run 3")
    assert "Job completed\n" in main_tester("SIESTAstepper single_run log 2 C")


def main_carbon_project_run_interrupted():
    """Run tests based on Carbon_uninterrupted run run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    assert "All iterations are completed" in main_tester("SIESTAstepper run_interrupted log 3 C cont=continue")
    assert ((expr in main_tester("SIESTAstepper analysis log")) for expr in [
        "-297.982681",
        "-299.171055",
        "-299.791356",
        "-299.845957",
        "-299.498399"
    ])
    assert ((expr in main_tester("SIESTAstepper energy_diff log")) for expr in [
        "-299.845957",
        "-297.982681",
        "1.863276"
    ])


def test_main_carbon_project_single_run_interrupted():
    """Run tests based on Carbon_uninterrupted run single_run_interrupted function with __main__.py"""
    fake_command()
    set_fake_project("Carbon")
    os.chdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{get_fake_project()}")
    settings.set_cwd(os.getcwd())
    assert ((expr in main_tester("SIESTAstepper make_directories 5")) for expr in [
        "i1 created",
        "i2 created",
        "i3 created",
        "i4 created",
        "i5 created"
    ])
    initialise_fake_project("single_run_interrupted 3 1")
    # assert "Job completed\n" in main_tester("SIESTAstepper single_run_interrupted log 3 C")
