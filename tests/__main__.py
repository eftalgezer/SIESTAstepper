"""
Evaluate unit tests for the SIESTAstepper library.
"""
from .tests import *

clear_temp()
test_ani_to_fdf()
test_xyz_to_fdf()
test_merge_ani()
clear_temp()
test_make_directories()
test_copy_files()
test_analysis()
test_energy_diff()
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
# test_carbon_project_single_run_interrupted()
# clear_temp()
test_main()
clear_temp()
test_main_carbon_uninterrupted_project()
clear_temp()
# test_main_carbon_uninterrupted_project_run_next()
# clear_temp()
# test_main_carbon_uninterrupted_project_single_run()
# clear_temp()
test_main_carbon_project_run_interrupted()
clear_temp()
# test_main_carbon_project_single_run_interrupted()
# clear_temp()
