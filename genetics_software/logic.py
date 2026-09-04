class mendelian_genetics:
    def __init__(self,p1,p2):
        #cross = input("Enter the cross here with the number of traits (eg- Aa,Aa,1): ")
        #process user input
        self.p1 = p1.strip()   
        self.p2 = p2.strip()
        self.letters_used = []

        #innitialise punnets square as a two dimentional list
        self.punnets_square = []


    def combine(self,group,index,current=""):  
        if index == len(group):
            return [current]
        result = []
        for i in group[index]:
            result.extend(self.combine(group, index + 1, current + i))
        return result
    
    def group(self,parent):
        #create a list of the letters used in the cross
        letters = []
        for i in parent:
            if i.lower() not in letters:
                letters.append(i.lower())

        #groups the letters of the parent together to show the number traits
        group = [[] for _ in range(len(letters))]
        for i in parent:
            for j in range(len(letters)):
                if i.lower() == letters[j]:
                    group[j].append(i)

        return group

    def find_genes(self,parent):
        group = self.group(parent)
        genes = self.combine(group,0)
        return genes
    
    def n_hibrid_cross(self):
        self.punnets_square = []
        p1_genes = self.find_genes(self.p1)
        p2_genes = self.find_genes(self.p2)
        for i in p1_genes:
            row = []
            for j in p2_genes:
                combined = i + j
                sorted_genes = "".join(sorted(combined, key=lambda x: (x.lower(), x.islower())))
                row.append(sorted_genes)
            self.punnets_square.append(row)

        return self.punnets_square
    
    def main_terminal(self): # for testing
        print_square = input("Do you want to see the punnets square? (y/n)")
        if print_square.lower() == "y":
            punnets_square = self.n_hibrid_cross()
            for row in punnets_square:
                print(" ".join(f"{cell:2}" for cell in row))

        info = input("Do you want to see the genotypic and phenotypic ratios of your cross? (y/n)")
        if info.lower() == "y":
            self.simplified_data()


    def simplified_data(self):
        for i in self.p1:
            if i.lower() not in self.letters_used:
                self.letters_used.append(i.lower())

        punnets_square = self.n_hibrid_cross()
        genotypes = {}
        for row in punnets_square:
            for cell in row:
                if cell not in genotypes:
                    genotypes[cell] = 1
                else:
                    genotypes[cell] += 1
        #print(f"The possible genotypes of the cross are: {genotypes}")  

        phenotypes = {}

        for key in genotypes:
            phenotype = ""

            for gene in self.letters_used:
                if gene.upper() in key:
                    phenotype += gene.upper()
                else:
                    phenotype += gene.lower()

            phenotypes[phenotype] = phenotypes.get(phenotype, 0) + genotypes[key]

        #print(f"The phenotypic ratio of the cross is: {phenotypes}")
        return genotypes,phenotypes
    

    def mono_cross(self,s1,s2):
        dom = 0
        rec = 0
        genes = []
        for i in s1:
            for j in s2:
                gene = i + j 
                genes.append(gene)

        for gene in genes:
            if any(letter.isupper() for letter in gene):
                dom += 1
            else:
                rec += 1

        phenotype_ratio = [dom, rec]
        return phenotype_ratio
    
    def fork_method(self,s1,s2):
        pheno_ratio = {}
        group1 = self.group(s1)
        group2 = self.group(s2)

        for i in range(len(group1)):
            cross =  self.mono_cross(group1[i], group2[i])
            pheno_ratio[f"Trait {i + 1}"] = cross 

        total_dom = 1
        for value in pheno_ratio.values():
            total_dom *= value[0]
        total_rec = 1
        for value in pheno_ratio.values():
            total_rec *= value[1]
        total = [total_dom, total_rec]
        return pheno_ratio, total

     
    


