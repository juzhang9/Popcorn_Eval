h1 = 0.5
h2 = 0.5
rho_ge = 0.5
m = 205452
p = 0.99
n1 = 26119
n2 = 20147

import numpy as np
eur_frq = np.loadtxt('/mnt/rstor/SOM_EPBI_FRS2/jxz617/simulationEUREAS8/EUR_PostFilterupd.frq', usecols = [4])
eur_sigma = 2 * eur_frq * (1 - eur_frq)
eas_frq = np.loadtxt('/mnt/rstor/SOM_EPBI_FRS2/jxz617/simulationEUREAS8/EAS_PostFilterupd.frq', usecols = [4])
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


temp1 = np.arange(-1, 1.1, 0.1) 
temp2 = np.append(np.insert(np.arange(0.1, 1, 0.1), 0, 0.0000001), 0.9999999)

rho_gi1 = []
for i in range(1, 22):
	rho_gi1 = rho_gi1 + [simu(temp1[i-1], m, h1, h2, p, i)]

np.savetxt('rho_gi1.txt',rho_gi1)

rho_gi2 = []
for i in range(22, 33):
	rho_gi2 = rho_gi2 + [simu(0.5, m, temp2[i-22], h2, p, i)]

np.savetxt('rho_gi2.txt',rho_gi2)

rho_gi3 = []
for i in range(33, 44):
	rho_gi3 = rho_gi3 + [simu(0.5, m, h1, temp2[i-33], p, i)]

np.savetxt('rho_gi3.txt',rho_gi3)

