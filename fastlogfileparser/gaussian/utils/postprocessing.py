from fastlogfileparser.generic.postprocessing import _charge_and_multiplicity, _unix_time_to_seconds, _str_to_float, _str_list_to_floats, _freq_modes, _columns_to_floats


POSTPROCESSING_FUNCTIONS = {
    "cpu_time": _unix_time_to_seconds,
    "wall_time": _unix_time_to_seconds,
    "e0": _str_to_float,
    "e0_h": _str_to_float,
    "hf": _str_to_float,
    "scf": _str_list_to_floats,
    "recovered_energy": _str_list_to_floats,
    "zpe_per_atom": _str_to_float,
    "wavefunction_energy": _str_to_float,
    "e0_zpe": _str_to_float,
    "gibbs": _str_to_float,
    "frequency_modes": _freq_modes,
    "frequencies": lambda in_list: [float(i) for sublist in in_list for i in sublist],
    "max_steps": lambda in_list: int(in_list[0]),
    "std_forces": _columns_to_floats,
    "std_xyz": _columns_to_floats,
    "xyz": _columns_to_floats,
    "route_section": lambda in_list: in_list[0],
    "charge_and_multiplicity": _charge_and_multiplicity,
    "normal_termination": lambda in_list: len(in_list) > 0,
}
