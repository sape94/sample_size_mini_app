import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


image = Image.open('iroh_the_cat.png')
st.image(image, use_column_width='always', output_format='PNG')

st.title('Sample Size Calculator.')

st.markdown('The **sample size\' formula** is the following:')
st.latex(r'n = \frac{NZ^{2}pq}{e^{2}(N-1)+Z^{2}pq};')
st.markdown('')
st.write(r'where $n$ is the sample size, $N$ the population size, $Z$ the $Z$-score value, $p$ the sample portion, $e$ the standard error, and $q=(1-p)$.')
st.markdown('')

with st.expander('If you want to upload a Dataframe, expand this section. When you finish you can collapse it again.'):
    st.write(
        'Upload the CSV file that contains the Dataframe with the feasibility information:')
    uploaded_file = st.file_uploader("Choose a file",
                                     type=['csv'],
                                     key='gral_seetings_df'
                                     )
    if uploaded_file is not None:
        feas_df = pd.read_csv(uploaded_file)
        file_name_df = uploaded_file.name
        st.write(feas_df)

st.markdown('')

col1, col2 = st.columns(2, gap='medium')

with col1:
    st.write('Select the **confidence level** (%):')
    conf_lev = st.selectbox(
        r'',
        ('99', '98', '95', '90', '80'))
    #    ('1', '2', '5', '10', '20'))
    e = (100 - int(conf_lev))/100

with col2:
    if e == 0.01:
        Z = 2.576
        st.write('Then, the $Z$-**score value** is:')
        z_box = st.selectbox(
            r'',
            ('2.576', '2.326', '1.960', '1.645', '1.282', '0.674'), disabled=True)
    if e == 0.02:
        Z = 2.326
        st.write('Then, the $Z$-**score value** is:')
        z_box = st.selectbox(
            r'',
            ('2.326', '2.576', '1.960', '1.645', '1.282', '0.674'), disabled=True)
    if e == 0.05:
        Z = 1.96
        st.write('Then, the $Z$-**score value** is:')
        z_box = st.selectbox(
            r'',
            ('1.960', '2.326', '1.645', '2.576', '1.282', '0.674'), disabled=True)
    if e == 0.1:
        Z = 1.645
        st.write('Then, the $Z$-**score value** is:')
        z_box = st.selectbox(
            r'',
            ('1.645', '2.576', '2.326', '1.960', '1.282', '0.674'), disabled=True)
    if e == 0.2:
        Z = 1.282
        st.write('Then, the $Z$-**score value** is:')
        z_box = st.selectbox(
            r'',
            ('1.282', '1.645', '2.576', '1.960', '2.326', '0.674'), disabled=True)

st.markdown('')
st.markdown('')

col3, col4 = st.columns(2, gap='medium')

with col3:
    if uploaded_file is not None:
        st.write(r'The **population size**, $N$, is:')
        N = feas_df.shape[0]
        N_s = str(N)
        z_box = st.selectbox(
            r'',
            (f'{N_s}', '4'), disabled=True)
    else:
        st.write(r'Type the **population size**, $N$:')
        N = st.number_input('', min_value=1)

p = 0.5
q = 1-p
n = int(N*(Z**2)*p*q/((e**2)*(N-1)+(Z**2)*p*q))

with col4:
    st.write(
        r':arrow_forward::arrow_forward: Then, the **sample size** is:')
    st.write('')
    st.latex(f'n = {n}')

st.markdown('')
st.markdown('')
st.markdown('')

if uploaded_file is not None:
    with st.expander('If you want to sample the Dataframe, expand this section. When you finish you can collapse it again.'):
        samp_ans = st.radio('Do you want to sample your Dataframe? (Non-stratified method)',
                            ('No', 'Yes'))
        if samp_ans == 'Yes':
            sampled_df = feas_df.sample(n=n)
            st.button(':inbox_tray: Press here to re-sample :inbox_tray:')
            st.write(sampled_df)
            sampled_df_csv = sampled_df.to_csv(index=False)
            col5, col6 = st.columns(2, gap='medium')
            with col6:
                st.download_button(label=':floppy_disk: Download Dataframe as CSV :floppy_disk:',
                                   data=sampled_df_csv,
                                   file_name=f'SAMPLED_{file_name_df}.csv',
                                   mime='text/csv')

col7, col8 = st.columns(2, gap='medium')


with col7:
    with st.expander('Complementary info'):
        st.write(r'$p=0.5$;')
        st.write(r'$q=0.5$;')
        st.write(
            r'Please note that the **confidence level** is equal to 100% minus the standard error.')

# st.info('This is a purely informational message', icon="ℹ️")

ft = """

<style>

footer {
    visibility:visible;
}
footer:after{
    content:'sape94';
    display:block;
    position:relative;
    top:2px;
}

</style>

"""
st.write(ft, unsafe_allow_html=True)
