import gauss_method as gm

# path of file of optical IOD-formatted observations
filename = '../example_data/iod_data_af2.txt'

#body name
# bodyname = '21799'

#lines of observations file to be used for orbit determination
obs_arr = [1, 3, 4, 6, 8] # LB observations of 21799 91 076C on 2018 Jul 22

###modify r2_root_ind_vec as necessary if adequate root of Gauss polynomial has to be selected
###if r2_root_ind_vec is not specified, then the first positive root will always be selected by default
# r2_root_ind_vec = zeros((len(obs_arr)-2,), dtype=int)
###select adequate index of Gauss polynomial root
# r2_root_ind_vec[4] = 1

index_pass, radius_pass, velocity_pass, inclination_pass, raan_pass, eccentricity_pass, AoP_pass, \
    mean_anomaly_pass, n_mean_motion_perday_pass, T_orbitperiod_pass = \
        gm.gauss_method_sat(filename, obs_arr, refiters=10, plot=True)
