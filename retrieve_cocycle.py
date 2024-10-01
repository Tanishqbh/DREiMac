from dreimac.utils import CohomologyUtils
def get_cocycle_as_matrix(cc):
    x,_ = zip(*cc.harm_reps)
    cocycle_as_vector = x[0]
    theta_mat = CohomologyUtils.one_cocycle_to_matrix(dist_mat=cc._dist_land_land,threshold= cc._rips_threshold, lookup_table=cc._cns_lookup_table, n_points=cc._n_landmarks, cocycle_as_vector=cocycle_as_vector)
    return theta_mat