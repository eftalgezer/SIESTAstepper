"""
Evaluate unit tests for the SIESTAstepper library.
"""
from __future__ import absolute_import
from .tests import (
    test_ani_to_fdf,
    test_xyz_to_fdf,
    test_xv_to_fdf,
    test_merge_ani,
    test_make_directories,
    test_copy_files,
    test_energy_analysis,
    test_force_analysis,
    test_energy_diff,
    test_force_diff,
    test_get_it,
    test_read_fdf,
    test_create_fdf,
    test_read_energy,
    test_print_run,
    test_check_restart,
    test_check_userbasis,
    test_sort_,
    test_remove_nones,
    test_carbon_uninterrupted_project,
    test_carbon_uninterrupted_project_run_next,
    test_carbon_uninterrupted_project_single_run,
    test_carbon_project_run_interrupted,
    test_carbon_project_single_run_interrupted,
    test_carbon_xv_uninterrupted_project,
    test_carbon_xv_uninterrupted_project_run_next,
    test_carbon_xv_uninterrupted_project_single_run,
    test_carbon_xv_project_run_interrupted,
    test_carbon_xv_project_single_run_interrupted,
    test_main,
    test_main_carbon_uninterrupted_project,
    test_main_carbon_uninterrupted_project_run_next,
    test_main_carbon_uninterrupted_project_single_run,
    test_main_carbon_project_run_interrupted,
    test_main_carbon_project_single_run_interrupted,
    test_main_carbon_xv_uninterrupted_project,
    test_main_carbon_xv_uninterrupted_project_run_next,
    test_main_carbon_xv_uninterrupted_project_single_run,
    test_main_carbon_xv_project_run_interrupted,
    test_main_carbon_xv_project_single_run_interrupted,
    TestErrors
)
from .testers import clear_temp

clear_temp()
test_ani_to_fdf()
test_xyz_to_fdf()
test_xv_to_fdf()
test_merge_ani()
clear_temp()
test_make_directories()
test_copy_files()
test_energy_analysis()
test_force_analysis()
test_energy_diff()
test_force_diff()
test_get_it()
test_read_fdf()
test_create_fdf()
test_read_energy()
test_print_run()
test_check_restart()
test_check_userbasis()
test_sort_()
test_remove_nones()
clear_temp()
test_carbon_uninterrupted_project()
clear_temp()
test_carbon_uninterrupted_project_run_next()
clear_temp()
test_carbon_uninterrupted_project_single_run()
clear_temp()
test_carbon_project_run_interrupted()
clear_temp()
test_carbon_project_single_run_interrupted()
clear_temp()
test_carbon_xv_uninterrupted_project()
clear_temp()
test_carbon_xv_uninterrupted_project_run_next()
clear_temp()
test_carbon_xv_uninterrupted_project_single_run()
clear_temp()
test_carbon_xv_project_run_interrupted()
clear_temp()
test_carbon_xv_project_single_run_interrupted()
clear_temp()
test_carbon_log_uninterrupted_project()
clear_temp()
test_carbon_log_uninterrupted_project_run_next()
clear_temp()
test_carbon_log_uninterrupted_project_single_run()
clear_temp()
test_carbon_log_project_run_interrupted()
clear_temp()
test_carbon_log_project_single_run_interrupted()
clear_temp()
test_main()
clear_temp()
test_main_carbon_uninterrupted_project()
clear_temp()
test_main_carbon_uninterrupted_project_run_next()
clear_temp()
test_main_carbon_uninterrupted_project_single_run()
clear_temp()
test_main_carbon_project_run_interrupted()
clear_temp()
test_main_carbon_project_single_run_interrupted()
clear_temp()
test_main_carbon_xv_uninterrupted_project()
clear_temp()
test_main_carbon_xv_uninterrupted_project_run_next()
clear_temp()
test_main_carbon_xv_uninterrupted_project_single_run()
clear_temp()
test_main_carbon_xv_project_run_interrupted()
clear_temp()
test_main_carbon_xv_project_single_run_interrupted()
clear_temp()
test_main_carbon_log_uninterrupted_project()
clear_temp()
test_main_carbon_log_uninterrupted_project_run_next()
clear_temp()
test_main_carbon_log_uninterrupted_project_single_run()
clear_temp()
test_main_carbon_log_project_run_interrupted()
clear_temp()
test_main_carbon_log_project_single_run_interrupted()
clear_temp()
testerrors = TestErrors()
testerrors.test_main()
testerrors.test_pair_correlation_function()
# testerrors.test_get_it()
testerrors.test_copy_file()
