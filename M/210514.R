args = commandArgs(trailingOnly=TRUE)
add1 <- args[1]
pop <- args[2]
ind1 <- args[3]
add2 <- args[4]
ind2 <- args[5]
add3 <- args[6]
ind3 <- args[7]

sumname <- paste(add1, pop, 'summarystat', ind1, sep = '')
snpname <- paste(add2, ind2, sep = '')
sum <- read.table(sumname, header = T)
snp <- read.table(snpname)

res <- merge(snp, sum, by.x = 'V1', by.y = 'rsid')
colnames(res)[1] <- 'rsid'

outname <- paste(add3, pop, 'partsumstat', ind3, sep = '')
write.table(res, outname, row.names = F, quote = F, sep = "\t")
