import streamlit as st
from logic import mendelian_genetics
import pandas as pd

st.title("Mendelian Genetics")

p1 = st.text_input("Enter genotype of first parent (eg. AaBb):")
p2 = st.text_input("Enter genotype of second parent (eg.AABb):")

if p1 and p2:
        cross = mendelian_genetics(p1, p2)
        square = cross.n_hibrid_cross()
        genotypes, phenotypes = cross.simplified_data()
        pheno_ratio, total = cross.fork_method(p1,p2)


if st.button("Display Punnett Square?"):
    p1_genes = cross.find_genes(p1)
    p2_genes = cross.find_genes(p2)

    df = pd.DataFrame(square)
    st.subheader("Punnett Square:")
    df.index = [f"{g}_{i}" for i, g in enumerate(p1_genes)] 
    df.columns = [f"{g}_{i}" for i, g in enumerate(p2_genes)] 
    st.table(df)

if st.button("Display Ratios?"):
    st.subheader("Genotype")
    geno_df = pd.DataFrame(list(genotypes.items()), columns=["Genotype", "Count"])
    st.table(geno_df)

    st.subheader("Phenotype")
    pheno_df = pd.DataFrame(list(phenotypes.items()), columns=["Phenotype", "Count"])
    st.table(pheno_df)

if st.button("Display Forked Line Diagram?"):
     st.subheader("Forked Line Diagram:")
     fork_df = pd.DataFrame(list(pheno_ratio.items()), columns=["Traits", "Count"])
     fork_df.loc[len(fork_df)] = ["Total", total]
     st.table(fork_df)


