import os

from fastlogfileparser.gaussian import fast_gaussian_logfile_parser


def test_fast_gaussian_logfile_parser():
    """
    Test parser using a log file with gaussian LINK of three consecutive semi-empirical level jobs AM1, PM7, XTB
    """

    file = os.path.join(
        os.path.dirname(__file__), "data", "ts_opt_three_step_semi_all_success.log"
    )
    job_1, job_2, job_3 = fast_gaussian_logfile_parser(file)
    assert job_1.normal_termination is True
    assert job_2.normal_termination is True
    assert job_3.normal_termination is True
    assert (
        job_1.route_section
        == "P opt=(ModRedundant,calcall,maxcycle=64,noeig,nomicro) scf=(xqc) iop(7/33=1) iop(2/9=2000) iop(7/127=-99) iop(8/117=-99) am1"
    )
    assert (
        job_2.route_section
        == "P opt=(ModRedundant,ts,calcall,maxcycle=64,noeig,nomicro) scf=(xqc) iop(7/33=1) iop(2/9=2000) geom=check guess=mix pm7"
    )
    assert job_3.route_section == (
        "P opt=(ts,calcall,maxcycle=90,noeig,nomicro,cartesian) scf=(xqc) iop(7/33=1) iop(2/9=2000) geom=check guess=mix external="
        '"/home/gridsan/groups/RMG/Software/RDMC-main/rdmc/external/xtb_tools/xtb_gaussian.pl --gfn 2 -P"'
    )
    assert job_1.charge_and_multiplicity == [0, 2]
    assert job_2.charge_and_multiplicity == [0, 2]
    assert job_3.charge_and_multiplicity == [0, 2]
    assert job_1.gibbs == 0.453491
    assert job_2.gibbs == 0.377958
    assert job_3.gibbs == -57.116221
    assert job_1.e0_zpe == 0.501018
    assert job_2.e0_zpe == 0.424827
    assert job_3.e0_zpe == -57.066865
    assert job_1.zpe_per_atom == 0.2756248
    assert job_2.zpe_per_atom == 0.2546919
    assert job_3.zpe_per_atom == 0.2611432
    assert job_1.e0_h == 0.519054
    assert job_2.e0_h == 0.442973
    assert job_3.e0_h == -57.047106
    assert job_1.hf == 0.2253936
    assert job_2.hf == 0.1701352
    assert job_3.hf == -57.3280082
    assert job_1.cpu_time == 1729.1
    assert job_2.cpu_time == 732.8
    assert job_3.cpu_time == 450.9
    assert job_1.wall_time == 133.3
    assert job_2.wall_time == 57.3
    assert job_3.wall_time == 67.0
    assert job_1.number_of_atoms == 35
    assert job_2.number_of_atoms == 35
    assert job_3.number_of_atoms == 35
    assert job_1.number_of_optimization_steps == 18
    assert job_2.number_of_optimization_steps == 9
    assert job_3.number_of_optimization_steps == 31
    assert job_1.recovered_energy is None
    assert job_2.recovered_energy is None
    assert job_3.recovered_energy[0] == -57.3069045667
    assert job_3.recovered_energy[1] == -57.3139032763
    assert job_3.recovered_energy[-2] == -57.328008209
    assert job_3.recovered_energy[-1] == -57.3280082435
    assert len(job_3.recovered_energy) == 31
    assert job_1.frequencies[0] == -2302.4897
    assert job_1.frequencies[-1] == 3367.7609
    assert len(job_1.frequencies) == 99
    assert job_2.frequencies[1] == -65.2439
    assert job_2.frequencies[-2] == 2772.4802
    assert len(job_2.frequencies) == 99
    assert job_3.frequencies == [
        -1070.248,
        21.2558,
        34.2835,
        38.4794,
        50.8615,
        66.318,
        72.0175,
        104.4354,
        126.2533,
        178.164,
        190.6464,
        201.5766,
        230.1125,
        244.0453,
        258.3915,
        288.0747,
        319.5283,
        331.1254,
        337.4849,
        362.0772,
        376.8511,
        380.6593,
        419.7345,
        480.4958,
        483.6609,
        516.5783,
        523.9647,
        539.752,
        560.1229,
        593.1202,
        618.2125,
        629.2787,
        665.2088,
        680.6649,
        699.5886,
        710.2207,
        768.6965,
        769.6295,
        825.1324,
        858.965,
        876.7569,
        896.6266,
        912.0599,
        913.4817,
        918.0845,
        923.8787,
        931.8196,
        1007.5661,
        1052.9469,
        1060.3788,
        1065.9656,
        1077.552,
        1092.4222,
        1099.997,
        1108.2718,
        1122.1112,
        1129.8856,
        1145.5331,
        1160.5772,
        1167.1457,
        1177.2996,
        1197.0858,
        1204.0635,
        1241.2318,
        1269.6735,
        1278.369,
        1285.7483,
        1298.9741,
        1343.8235,
        1366.2008,
        1380.2288,
        1392.7438,
        1400.2953,
        1420.7035,
        1433.8104,
        1437.2969,
        1466.1181,
        1472.7239,
        1480.3023,
        1492.9849,
        1561.163,
        1584.5292,
        1586.8818,
        1598.23,
        1676.3884,
        2926.8699,
        2958.67,
        2992.993,
        3055.6369,
        3071.0991,
        3078.5004,
        3090.5944,
        3099.3502,
        3103.0384,
        3103.9318,
        3108.6467,
        3144.2251,
        3148.1604,
        3481.313,
    ]
    assert len(job_3.frequencies) == 99
    assert len(job_1.std_forces) == 19
    assert len(job_1.std_forces[0]) == 35
    assert job_1.std_forces[0][0] == [
        1.0,
        1.0,
        -0.012034736,
        0.000231533,
        -0.008718935,
    ]
    assert job_1.std_forces[0][-1] == [
        35.0,
        1.0,
        0.002160253,
        -0.010676581,
        -0.009002864,
    ]
    assert job_1.std_forces[-1][0] == [1.0, 1.0, -8e-08, -9e-09, 1.92e-07]
    assert job_1.std_forces[-1][-1] == [35.0, 1.0, -2.2e-08, 1.8e-08, -1e-09]
    assert len(job_2.std_forces) == 10
    assert len(job_2.std_forces[0]) == 35
    assert job_2.std_forces[0][0] == [
        1.0,
        1.0,
        0.013295924,
        -0.000472478,
        0.000883286,
    ]
    assert job_2.std_forces[0][-1] == [
        35.0,
        1.0,
        -0.000877563,
        0.001225992,
        0.003512116,
    ]
    assert job_2.std_forces[-1][0] == [1.0, 1.0, 2.06e-07, -1.15e-07, -2.2e-08]
    assert job_2.std_forces[-1][-1] == [35.0, 1.0, 6e-09, 5e-09, 2e-09]
    assert len(job_3.std_forces) == 32
    assert len(job_3.std_forces[0]) == 35
    assert job_3.std_forces[0][0] == [
        1.0,
        1.0,
        -0.016887644,
        -0.00517337,
        -0.008264572,
    ]
    assert job_3.std_forces[0][-1] == [
        35.0,
        1.0,
        -0.001623912,
        0.006837508,
        0.008029253,
    ]
    assert job_3.std_forces[-1][0] == [1.0, 1.0, -5.19e-07, -2.07e-07, 3.29e-07]
    assert job_3.std_forces[-1][-1] == [35.0, 1.0, 1.95e-07, -5.4e-08, 8.3e-08]
    assert len(job_1.std_xyz) == 19
    assert len(job_1.std_xyz[0]) == 35
    assert job_1.std_xyz[0][0] == [1.0, 1.0, 0.0, -0.274545, -2.553625, 1.166114]
    assert job_1.std_xyz[0][-1] == [35.0, 1.0, 0.0, -3.902734, 2.175794, 1.493715]
    assert job_1.std_xyz[1][0] == [1.0, 1.0, 0.0, 0.104125, -2.044038, 1.430378]
    assert job_1.std_xyz[1][-1] == [35.0, 1.0, 0.0, -4.005975, 1.944035, 1.575083]
    assert job_1.std_xyz[-1][0] == [1.0, 1.0, 0.0, 2.288411, -1.715873, 2.983735]
    assert job_1.std_xyz[-1][-1] == [35.0, 1.0, 0.0, -3.483513, 0.579376, 2.671913]
    assert len(job_2.std_xyz) == 10
    assert len(job_2.std_xyz[0]) == 35
    assert job_2.std_xyz[0][0] == [1.0, 1.0, 0.0, 2.288411, -1.715873, 2.983735]
    assert job_2.std_xyz[0][-1] == [35.0, 1.0, 0.0, -3.483513, 0.579376, 2.671913]
    assert job_2.std_xyz[1][0] == [1.0, 1.0, 0.0, 1.46839, -1.948579, 2.481679]
    assert job_2.std_xyz[1][-1] == [35.0, 1.0, 0.0, -3.336096, 0.644271, 2.658772]
    assert job_2.std_xyz[-1][0] == [1.0, 1.0, 0.0, 0.277827, -0.733444, 2.34837]
    assert job_2.std_xyz[-1][-1] == [35.0, 1.0, 0.0, -3.292172, 2.078041, 1.982963]
    assert len(job_3.std_xyz) == 32
    assert len(job_3.std_xyz[0]) == 35
    assert job_3.std_xyz[0][0] == [1.0, 1.0, 0.0, 0.277827, -0.733444, 2.34837]
    assert job_3.std_xyz[0][-1] == [35.0, 1.0, 0.0, -3.292172, 2.078041, 1.982963]
    assert job_3.std_xyz[1][0] == [1.0, 1.0, 0.0, 0.322829, -0.775239, 2.426687]
    assert job_3.std_xyz[1][-1] == [35.0, 1.0, 0.0, -3.297056, 2.031193, 1.995294]
    assert job_3.std_xyz[-1][0] == [1.0, 1.0, 0.0, 1.785766, -1.923322, 2.412318]
    assert job_3.std_xyz[-1][-1] == [35.0, 1.0, 0.0, -4.255334, 1.709578, 1.25933]
    assert len(job_1.xyz) == 19
    assert len(job_1.xyz[0]) == 35
    assert job_1.xyz[0] == [
        [1.0, 1.0, 0.0, -0.685827, 1.281098, 0.993117],
        [2.0, 8.0, 0.0, 0.282333, 0.454653, -0.531484],
        [3.0, 8.0, 0.0, 0.032084, 1.524857, 0.372679],
        [4.0, 7.0, 0.0, -2.251385, -1.506529, -0.269281],
        [5.0, 7.0, 0.0, -3.643363, 0.259986, 0.208542],
        [6.0, 7.0, 0.0, -1.876414, -0.197147, 1.767129],
        [7.0, 7.0, 0.0, -4.830772, 2.343331, 0.078931],
        [8.0, 6.0, 0.0, -0.890949, -1.809402, -0.685049],
        [9.0, 6.0, 0.0, -0.85843, -1.101086, 2.273594],
        [10.0, 6.0, 0.0, -3.173691, -1.361721, -1.330426],
        [11.0, 6.0, 0.0, -4.030871, -0.289132, -1.041317],
        [12.0, 6.0, 0.0, -2.523242, -0.481582, 0.68225],
        [13.0, 6.0, 0.0, -4.208983, 1.400641, 0.838576],
        [14.0, 6.0, 0.0, -5.051916, 0.056537, -1.908798],
        [15.0, 6.0, 0.0, -3.326203, -2.107799, -2.487223],
        [16.0, 6.0, 0.0, -4.164939, 1.563181, 2.22734],
        [17.0, 6.0, 0.0, -4.724558, 2.691777, 2.830231],
        [18.0, 6.0, 0.0, -5.205612, -0.683427, -3.084837],
        [19.0, 6.0, 0.0, -4.350264, -1.757896, -3.371327],
        [20.0, 6.0, 0.0, -5.332709, 3.651664, 2.040549],
        [21.0, 6.0, 0.0, -5.362433, 3.432163, 0.679269],
        [22.0, 1.0, 0.0, -0.152123, -0.663302, -0.776045],
        [23.0, 1.0, 0.0, -0.804732, -2.296992, -1.661596],
        [24.0, 1.0, 0.0, -0.382917, -2.451722, 0.039787],
        [25.0, 1.0, 0.0, -0.725911, -0.91287, 3.344093],
        [26.0, 1.0, 0.0, -1.147776, -2.152301, 2.176818],
        [27.0, 1.0, 0.0, 0.108545, -0.925978, 1.794821],
        [28.0, 1.0, 0.0, -3.721105, 0.807456, 2.866516],
        [29.0, 1.0, 0.0, -4.684515, 2.808175, 3.909428],
        [30.0, 1.0, 0.0, -5.775815, 4.540964, 2.472892],
        [31.0, 1.0, 0.0, -5.725406, 0.878601, -1.694563],
        [32.0, 1.0, 0.0, -6.000513, -0.425654, -3.781039],
        [33.0, 1.0, 0.0, -4.492757, -2.328099, -4.286496],
        [34.0, 1.0, 0.0, -2.691067, -2.958123, -2.706509],
        [35.0, 1.0, 0.0, -5.829554, 4.146093, 0.007037],
    ]
    assert len(job_2.xyz) == 10
    assert len(job_2.xyz[0]) == 35
    assert job_2.xyz[1] == [
        [1.0, 1.0, 0.0, -0.026543, 1.559817, -0.795496],
        [2.0, 8.0, 0.0, 0.8069, -0.078595, -0.680779],
        [3.0, 8.0, 0.0, 0.375637, 0.941727, -1.45434],
        [4.0, 7.0, 0.0, -2.201407, -1.312788, -0.325969],
        [5.0, 7.0, 0.0, -4.021185, -0.161056, 0.567202],
        [6.0, 7.0, 0.0, -2.108753, -0.315467, 1.966785],
        [7.0, 7.0, 0.0, -4.373636, 2.183848, 0.253664],
        [8.0, 6.0, 0.0, -0.970021, -1.90388, -0.488426],
        [9.0, 6.0, 0.0, -0.781134, -0.678582, 2.377951],
        [10.0, 6.0, 0.0, -3.174959, -1.188581, -1.341315],
        [11.0, 6.0, 0.0, -4.273086, -0.445325, -0.810897],
        [12.0, 6.0, 0.0, -2.652065, -0.586117, 0.83989],
        [13.0, 6.0, 0.0, -4.384383, 1.122763, 1.094057],
        [14.0, 6.0, 0.0, -5.395024, -0.18364, -1.57887],
        [15.0, 6.0, 0.0, -3.196767, -1.663947, -2.644548],
        [16.0, 6.0, 0.0, -4.760752, 1.211251, 2.446479],
        [17.0, 6.0, 0.0, -5.145038, 2.458978, 2.931547],
        [18.0, 6.0, 0.0, -5.410314, -0.672197, -2.890992],
        [19.0, 6.0, 0.0, -4.335571, -1.393151, -3.411174],
        [20.0, 6.0, 0.0, -5.147726, 3.559747, 2.076509],
        [21.0, 6.0, 0.0, -4.754614, 3.375701, 0.743142],
        [22.0, 1.0, 0.0, -0.088209, -0.905746, -0.794734],
        [23.0, 1.0, 0.0, -0.844214, -2.515371, -1.390082],
        [24.0, 1.0, 0.0, -0.476731, -2.29591, 0.405274],
        [25.0, 1.0, 0.0, -0.589403, -0.140152, 3.33449],
        [26.0, 1.0, 0.0, -0.679857, -1.763621, 2.580599],
        [27.0, 1.0, 0.0, 0.005966, -0.367968, 1.656735],
        [28.0, 1.0, 0.0, -4.732179, 0.328348, 3.08754],
        [29.0, 1.0, 0.0, -5.439619, 2.569641, 3.977629],
        [30.0, 1.0, 0.0, -5.443202, 4.545108, 2.431175],
        [31.0, 1.0, 0.0, -6.231139, 0.39089, -1.180685],
        [32.0, 1.0, 0.0, -6.282697, -0.47693, -3.5176],
        [33.0, 1.0, 0.0, -4.378414, -1.755264, -4.440389],
        [34.0, 1.0, 0.0, -2.361697, -2.222314, -3.064184],
        [35.0, 1.0, 0.0, -4.731955, 4.209199, 0.027422],
    ]
    assert len(job_3.xyz) == 32
    assert len(job_3.xyz[0]) == 35
    assert job_3.xyz[-1] == [
        [1.0, 1.0, 0.0, 0.261758, 1.177112, -0.548527],
        [2.0, 8.0, 0.0, 0.745479, -0.574321, -1.041625],
        [3.0, 8.0, 0.0, -0.019596, 0.573298, -1.25073],
        [4.0, 7.0, 0.0, -2.211764, -1.28394, -0.297995],
        [5.0, 7.0, 0.0, -3.655424, 0.33813, 0.297466],
        [6.0, 7.0, 0.0, -1.944001, -0.081389, 1.806119],
        [7.0, 7.0, 0.0, -5.092337, 2.13712, 0.283995],
        [8.0, 6.0, 0.0, -1.129849, -2.154884, -0.329376],
        [9.0, 6.0, 0.0, -0.73964, -0.64677, 2.332096],
        [10.0, 6.0, 0.0, -3.090977, -1.098156, -1.343025],
        [11.0, 6.0, 0.0, -4.000963, -0.092303, -0.977375],
        [12.0, 6.0, 0.0, -2.517241, -0.355322, 0.710019],
        [13.0, 6.0, 0.0, -4.301828, 1.350199, 1.00503],
        [14.0, 6.0, 0.0, -5.026306, 0.271375, -1.830989],
        [15.0, 6.0, 0.0, -3.175444, -1.738314, -2.569467],
        [16.0, 6.0, 0.0, -4.149764, 1.512273, 2.385036],
        [17.0, 6.0, 0.0, -4.83787, 2.54003, 2.999857],
        [18.0, 6.0, 0.0, -5.108701, -0.377149, -3.053745],
        [19.0, 6.0, 0.0, -4.198094, -1.360121, -3.420661],
        [20.0, 6.0, 0.0, -5.654828, 3.369304, 2.24306],
        [21.0, 6.0, 0.0, -5.745145, 3.113852, 0.886691],
        [22.0, 1.0, 0.0, -0.073673, -1.421413, -0.720914],
        [23.0, 1.0, 0.0, -1.224998, -2.905299, -1.103399],
        [24.0, 1.0, 0.0, -0.849007, -2.560162, 0.631473],
        [25.0, 1.0, 0.0, -0.441059, -0.009306, 3.165967],
        [26.0, 1.0, 0.0, -0.909434, -1.654458, 2.724124],
        [27.0, 1.0, 0.0, 0.078389, -0.685018, 1.609106],
        [28.0, 1.0, 0.0, -3.504246, 0.854467, 2.937701],
        [29.0, 1.0, 0.0, -4.741294, 2.690479, 4.065276],
        [30.0, 1.0, 0.0, -6.203504, 4.18129, 2.692587],
        [31.0, 1.0, 0.0, -5.72258, 1.042235, -1.55284],
        [32.0, 1.0, 0.0, -5.89737, -0.105314, -3.738331],
        [33.0, 1.0, 0.0, -4.286628, -1.836519, -4.384844],
        [34.0, 1.0, 0.0, -2.467614, -2.496701, -2.862313],
        [35.0, 1.0, 0.0, -6.368236, 3.716111, 0.238162],
    ]
    assert job_1.max_steps == 64
    assert job_2.max_steps == 64
    assert job_3.max_steps == 90
    assert len(job_1.frequency_modes) == 99
    assert len(job_2.frequency_modes) == 99
    assert len(job_3.frequency_modes) == 99
    assert job_3.frequency_modes[-1] == [
        [1.0, 1.0, 0.55, 0.78, -0.3],
        [2.0, 8.0, -0.0, 0.0, 0.0],
        [3.0, 8.0, -0.03, -0.05, 0.02],
        [4.0, 7.0, -0.0, -0.0, 0.0],
        [5.0, 7.0, -0.0, -0.0, -0.0],
        [6.0, 7.0, -0.0, 0.0, 0.0],
        [7.0, 7.0, -0.0, 0.0, 0.0],
        [8.0, 6.0, 0.0, -0.0, 0.0],
        [9.0, 6.0, 0.0, 0.0, -0.0],
        [10.0, 6.0, -0.0, 0.0, 0.0],
        [11.0, 6.0, 0.0, 0.0, 0.0],
        [12.0, 6.0, 0.0, -0.0, 0.0],
        [13.0, 6.0, 0.0, 0.0, -0.0],
        [14.0, 6.0, 0.0, -0.0, -0.0],
        [15.0, 6.0, -0.0, -0.0, 0.0],
        [16.0, 6.0, -0.0, -0.0, 0.0],
        [17.0, 6.0, 0.0, 0.0, -0.0],
        [18.0, 6.0, 0.0, -0.0, -0.0],
        [19.0, 6.0, -0.0, 0.0, 0.0],
        [20.0, 6.0, 0.0, 0.0, 0.0],
        [21.0, 6.0, -0.0, -0.0, -0.0],
        [22.0, 1.0, -0.0, -0.0, -0.0],
        [23.0, 1.0, 0.0, 0.0, -0.0],
        [24.0, 1.0, 0.0, 0.0, 0.0],
        [25.0, 1.0, -0.0, -0.0, -0.0],
        [26.0, 1.0, -0.0, -0.0, -0.0],
        [27.0, 1.0, 0.0, 0.0, 0.0],
        [28.0, 1.0, 0.0, -0.0, -0.0],
        [29.0, 1.0, -0.0, -0.0, -0.0],
        [30.0, 1.0, -0.0, -0.0, 0.0],
        [31.0, 1.0, 0.0, -0.0, 0.0],
        [32.0, 1.0, 0.0, 0.0, 0.0],
        [33.0, 1.0, 0.0, 0.0, 0.0],
        [34.0, 1.0, 0.0, -0.0, -0.0],
        [35.0, 1.0, -0.0, 0.0, 0.0],
    ]


def test_fast_gaussian_logfile_parser_2():
    """
    Test parser using a gaussian log file for a DFT optimization that failed.
    """

    file = os.path.join(os.path.dirname(__file__), "data", "non_ts_opt_failed.log")
    job = fast_gaussian_logfile_parser(file)[0]
    assert job.route_section == (
        "P opt=(calcfc,maxcycle=128,noeig,nomicro,cartesian) freq scf=(xqc)"
        " iop(7/33=1) iop(2/9=2000) guess=mix wb97xd/def2svp"
    )
    assert job.normal_termination is False
    assert job.charge_and_multiplicity == [0, 1]
    assert len(job.scf) == job.number_of_optimization_steps


def test_fast_gaussian_logfile_parser_3():
    """
    Test parser using a gaussian log file for a DFT optimization that succeed.
    """

    file = os.path.join(os.path.dirname(__file__), "data", "non_ts_opt_success.log")
    job = fast_gaussian_logfile_parser(file)[0]
    assert job.normal_termination is True
    assert job.charge_and_multiplicity == [0, 1]
    assert (
        job.route_section
        == "P opt=(calcfc,maxcycle=128,noeig,nomicro,cartesian) freq scf=(xqc) iop(7/33=1) iop(2/9=2000) guess=mix wb97xd/def2svp"
    )
    assert len(job.scf) == 26
    assert job.scf == [
        402.853361198,
        402.854751059,
        402.85564611,
        402.855063686,
        402.855709972,
        402.855740995,
        402.855798573,
        402.855811324,
        402.855831372,
        402.855832066,
        402.855832694,
        402.855832867,
        402.855832932,
        402.855832897,
        402.855832943,
        402.855832934,
        402.855832948,
        402.855832932,
        402.855832948,
        402.855832934,
        402.855832949,
        402.855832927,
        402.855832949,
        402.855832924,
        402.855832948,
        402.855832948,
    ]
    assert job.cpu_time == 4284.2
    assert job.wall_time == 293.4
    assert job.gibbs == -402.715409
    assert job.e0_zpe == -402.682224
    assert job.e0_h == -402.672907
    assert job.hf == -402.8558329
    assert job.zpe_per_atom == 0.1736092  # (Hartree/Particle)
    assert job.recovered_energy is None
    assert job.frequencies == [
        72.9396,
        96.8683,
        192.394,
        207.9457,
        272.2394,
        342.6685,
        368.4425,
        401.0024,
        478.0251,
        528.4524,
        687.6401,
        778.694,
        798.6369,
        827.0999,
        882.09,
        924.1866,
        955.4838,
        958.2687,
        977.133,
        991.5038,
        1001.9804,
        1032.0464,
        1048.1294,
        1069.6775,
        1100.2759,
        1113.9326,
        1123.2531,
        1154.0342,
        1189.903,
        1214.0463,
        1279.4557,
        1301.6757,
        1325.9641,
        1368.4872,
        1380.3865,
        1395.7035,
        1399.1188,
        1437.375,
        1467.5414,
        1475.764,
        1511.4812,
        1522.2826,
        1733.6455,
        2994.9671,
        3017.6716,
        3048.9327,
        3058.5047,
        3119.3761,
        3137.8986,
        3170.6442,
        3217.5738,
        3236.2974,
        3260.4636,
        3555.4258,
    ]
    assert len(job.frequencies) == 54
    assert len(job.std_forces) == 25
    assert job.std_forces[0] == [
        [1.0, 6.0, 0.007904782, 0.007077733, -0.000768348],
        [2.0, 6.0, 0.002319393, -0.001730758, 0.002172075],
        [3.0, 6.0, -0.001626312, 0.008349336, -0.002861984],
        [4.0, 6.0, -0.004130694, 0.0053082, 0.006513983],
        [5.0, 6.0, 0.001390514, 0.008734377, 0.003601166],
        [6.0, 6.0, -0.005109581, 0.001488587, 0.004337294],
        [7.0, 8.0, -0.001409035, -0.008096009, -0.00437355],
        [8.0, 6.0, 0.000449033, 0.000290382, 0.005219491],
        [9.0, 7.0, -0.010667798, 0.003144316, 0.005610324],
        [10.0, 1.0, -0.001701043, -0.003242709, 0.008302523],
        [11.0, 1.0, -0.007661417, 0.001636391, -0.002256312],
        [12.0, 1.0, 0.00133244, -0.007744441, -0.004276683],
        [13.0, 1.0, -0.001047373, -0.001262098, 0.003040266],
        [14.0, 1.0, -0.002171158, -0.012184887, -0.00418233],
        [15.0, 1.0, 0.007794641, -0.006640747, -0.00781197],
        [16.0, 1.0, 0.00149834, 0.003126533, -0.002696329],
        [17.0, 1.0, 0.004330705, 0.001285126, 0.001473196],
        [18.0, 1.0, -0.006024712, -0.001405932, -0.007458332],
        [19.0, 1.0, 0.008439219, 0.0028354, -0.001547936],
        [20.0, 1.0, 0.006090055, -0.000968801, -0.002036544],
    ]
    assert job.std_forces[-1] == [
        [1.0, 6.0, 1.736e-06, -4.121e-06, -1.746e-06],
        [2.0, 6.0, 1.6e-07, -1.898e-06, -1.1e-07],
        [3.0, 6.0, 5.23e-07, -1.106e-06, -7.55e-07],
        [4.0, 6.0, 1.903e-06, 2.167e-06, -3.055e-06],
        [5.0, 6.0, 8.91e-07, 4.5e-06, -1.42e-06],
        [6.0, 6.0, -1.024e-06, 3.215e-06, 2.119e-06],
        [7.0, 8.0, -1.244e-06, -4.57e-07, 2.325e-06],
        [8.0, 6.0, -1.448e-06, 1.05e-07, 1.802e-06],
        [9.0, 7.0, -2.411e-06, -3.37e-06, 2.697e-06],
        [10.0, 1.0, 6.65e-07, -1.866e-06, -1.272e-06],
        [11.0, 1.0, 5.84e-07, -1.88e-06, -6.95e-07],
        [12.0, 1.0, 9.95e-07, -3.65e-07, -8.89e-07],
        [13.0, 1.0, 5.52e-07, -1.897e-06, -8.69e-07],
        [14.0, 1.0, 1.152e-06, 1.175e-06, -2.971e-06],
        [15.0, 1.0, 5.03e-07, 3.259e-06, -1.269e-06],
        [16.0, 1.0, -6.46e-07, 2.323e-06, 2.077e-06],
        [17.0, 1.0, -6.28e-07, 6.54e-07, 1.203e-06],
        [18.0, 1.0, -4.91e-07, -4.6e-08, 7.1e-07],
        [19.0, 1.0, -9.25e-07, 6.29e-07, 7.72e-07],
        [20.0, 1.0, -8.49e-07, -1.023e-06, 1.348e-06],
    ]
    assert len(job.std_xyz) == 27
    assert job.std_xyz[0] == [
        [1.0, 6.0, 0.0, 2.17146, 1.203793, -0.202192],
        [2.0, 6.0, 0.0, 1.17511, 0.076574, -0.062046],
        [3.0, 6.0, 0.0, -0.207337, 0.370451, -0.658537],
        [4.0, 6.0, 0.0, -1.01882, 1.296816, 0.198804],
        [5.0, 6.0, 0.0, -2.136493, 0.699131, 0.570025],
        [6.0, 6.0, 0.0, -2.195167, -0.672025, -0.026029],
        [7.0, 8.0, 0.0, -0.987059, -0.818646, -0.754264],
        [8.0, 6.0, 0.0, 1.250142, -0.83467, 1.102254],
        [9.0, 7.0, 0.0, 1.706362, -1.257315, -0.206832],
        [10.0, 1.0, 0.0, 2.235021, 1.526151, -1.239633],
        [11.0, 1.0, 0.0, 3.15085, 0.855349, 0.111786],
        [12.0, 1.0, 0.0, 1.881733, 2.05348, 0.412837],
        [13.0, 1.0, 0.0, -0.06223, 0.77874, -1.672896],
        [14.0, 1.0, 0.0, -0.678593, 2.282877, 0.449088],
        [15.0, 1.0, 0.0, -2.92222, 1.081547, 1.193656],
        [16.0, 1.0, 0.0, -2.267394, -1.457608, 0.739689],
        [17.0, 1.0, 0.0, -3.047676, -0.785934, -0.71086],
        [18.0, 1.0, 0.0, 2.037482, -0.692555, 1.830556],
        [19.0, 1.0, 0.0, 0.333186, -1.245759, 1.506709],
        [20.0, 1.0, 0.0, 1.058421, -1.886332, -0.672677],
    ]
    assert job.std_xyz[-1] == [
        [1.0, 6.0, 0.0, 2.167612, 1.223055, -0.194553],
        [2.0, 6.0, 0.0, 1.18666, 0.084602, -0.049209],
        [3.0, 6.0, 0.0, -0.199375, 0.366547, -0.634572],
        [4.0, 6.0, 0.0, -1.038503, 1.298339, 0.199282],
        [5.0, 6.0, 0.0, -2.171827, 0.69424, 0.544273],
        [6.0, 6.0, 0.0, -2.203245, -0.686145, -0.04474],
        [7.0, 8.0, 0.0, -0.964246, -0.822918, -0.711082],
        [8.0, 6.0, 0.0, 1.26805, -0.854986, 1.0924],
        [9.0, 7.0, 0.0, 1.728116, -1.251667, -0.236824],
        [10.0, 1.0, 0.0, 2.300169, 1.487854, -1.255697],
        [11.0, 1.0, 0.0, 3.147686, 0.927178, 0.202702],
        [12.0, 1.0, 0.0, 1.829569, 2.121095, 0.346104],
        [13.0, 1.0, 0.0, -0.054261, 0.768232, -1.658665],
        [14.0, 1.0, 0.0, -0.730943, 2.309215, 0.467236],
        [15.0, 1.0, 0.0, -2.974014, 1.110169, 1.154905],
        [16.0, 1.0, 0.0, -2.310648, -1.472628, 0.725223],
        [17.0, 1.0, 0.0, -3.036919, -0.814141, -0.761121],
        [18.0, 1.0, 0.0, 2.048995, -0.72818, 1.84933],
        [19.0, 1.0, 0.0, 0.330741, -1.281243, 1.466248],
        [20.0, 1.0, 0.0, 1.010553, -1.83645, -0.667129],
    ]
    assert job.max_steps == 120
    assert job.frequency_modes[0] == [
        [1.0, 6.0, -0.08, 0.06, 0.18],
        [2.0, 6.0, -0.02, -0.02, 0.01],
        [3.0, 6.0, 0.0, -0.05, -0.04],
        [4.0, 6.0, 0.0, 0.06, -0.17],
        [5.0, 6.0, 0.01, 0.1, -0.07],
        [6.0, 6.0, 0.03, 0.01, 0.15],
        [7.0, 8.0, -0.02, -0.05, 0.08],
        [8.0, 6.0, 0.0, -0.12, -0.08],
        [9.0, 7.0, 0.07, 0.03, -0.1],
        [10.0, 1.0, -0.12, 0.26, 0.23],
        [11.0, 1.0, -0.05, 0.03, 0.09],
        [12.0, 1.0, -0.1, -0.06, 0.36],
        [13.0, 1.0, 0.03, -0.18, -0.09],
        [14.0, 1.0, -0.01, 0.11, -0.33],
        [15.0, 1.0, 0.02, 0.18, -0.12],
        [16.0, 1.0, 0.11, 0.13, 0.29],
        [17.0, 1.0, -0.02, -0.15, 0.24],
        [18.0, 1.0, -0.03, -0.15, -0.04],
        [19.0, 1.0, 0.02, -0.22, -0.15],
        [20.0, 1.0, 0.11, 0.03, -0.17],
    ]
    assert job.frequency_modes[-1] == [
        [1.0, 6.0, 0.0, 0.0, -0.0],
        [2.0, 6.0, -0.0, 0.0, 0.0],
        [3.0, 6.0, -0.0, 0.0, -0.0],
        [4.0, 6.0, -0.0, -0.0, -0.0],
        [5.0, 6.0, 0.0, 0.0, 0.0],
        [6.0, 6.0, -0.0, -0.0, 0.0],
        [7.0, 8.0, -0.0, 0.0, -0.0],
        [8.0, 6.0, -0.0, -0.0, 0.0],
        [9.0, 7.0, -0.05, -0.04, -0.03],
        [10.0, 1.0, 0.0, 0.0, -0.0],
        [11.0, 1.0, 0.0, 0.0, 0.0],
        [12.0, 1.0, -0.0, 0.0, 0.0],
        [13.0, 1.0, 0.0, -0.0, 0.0],
        [14.0, 1.0, 0.0, -0.0, -0.0],
        [15.0, 1.0, 0.0, -0.0, 0.0],
        [16.0, 1.0, 0.0, 0.0, -0.0],
        [17.0, 1.0, 0.0, 0.0, 0.0],
        [18.0, 1.0, 0.01, 0.0, 0.01],
        [19.0, 1.0, 0.01, 0.0, -0.0],
        [20.0, 1.0, 0.69, 0.58, 0.42],
    ]
    assert len(job.frequency_modes) == 54
    assert job.number_of_atoms == 20
    assert job.number_of_optimization_steps == 26
