import sys

pop1 = sys.argv[1]
pop2 = sys.argv[2]
h1 = float(sys.argv[3])
h2 = float(sys.argv[4])
m = int(float(sys.argv[5]))
p = float(sys.argv[6])
n1 = int(float(sys.argv[7]))
n2 = int(float(sys.argv[8]))
rho_ge0 = float(sys.argv[9])
ind = int(float(sys.argv[10]))


import numpy as np
temp01 = '%s' %ind
eurfrqname = '../../snp' + temp01 + '/' + pop1 + '_PostFilterupd.frq'
eur_frq = np.loadtxt(eurfrqname, usecols = [4])
eur_sigma = 2 * eur_frq * (1 - eur_frq)
easfrqname = '../../snp' + temp01 + '/' + pop2 + '_PostFilterupd.frq'
eas_frq = np.loadtxt(easfrqname, usecols = [4])
eas_sigma = 2 * eas_frq * (1 - eas_frq)
def simu(rho_ge, m, h1, h2, p, ind):
	binosample = np.random.binomial(1, p, m)
	sigma = [[h1/m, rho_ge * (h1 * h2) ** 0.5/m], [rho_ge * (h1 * h2) ** 0.5/m, h2/m]]
	beta = np.array([[0, 0]])
	for i in range(0, m):
		if binosample[i] == 1:
			beta = np.concatenate((beta, np.random.multivariate_normal([0, 0], sigma, 1)))
		else:
			beta = np.concatenate((beta, np.array([[0, 0]])))
	
	beta = beta[1:]
	temp = '%s' %ind
	beta_textname = "beta" + temp + ".txt"
	np.savetxt(beta_textname, beta)
	#rho_gi = np.corrcoef(eur_sigma ** 0.5 * beta[:, 0], eas_sigma ** 0.5 * beta[:, 1])[0, 1]
	eur_beta = eur_sigma ** 0.5 * beta[:, 0]
	eas_beta = eas_sigma ** 0.5 * beta[:, 1]
	rho_gi = np.sum(eur_beta * eas_beta)/np.sqrt(np.sum(eur_beta ** 2) * np.sum(eas_beta ** 2))
	return(rho_gi)

rho_gi = simu(rho_ge0, m, h1, h2, p, ind)
temp = '%s' %ind
rhogi_textname = "rho_gi" + temp + ".txt"
np.savetxt(rhogi_textname,[rho_gi])
