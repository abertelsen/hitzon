import random

import streamlit as st

import utils

def puzzle(text, target):
    st.title(':owl:')

    st.header('Traduce esta oración:')

    # st.markdown(text)

    # SETUP
    if not 'checked' in st.session_state:
        st.session_state.checked = False

    # TODO Add distractors.

    if not 'pieces' in st.session_state:
        st.session_state.pieces = utils.to_list(target)
        random.shuffle(st.session_state.pieces)  # Works in place, no return.

    answer_list = st.multiselect(label=text,
                                 options=st.session_state.pieces,
                                 disabled=st.session_state.checked)

    st.button(label='Comprobar', use_container_width=True, type='primary', 
              disabled = st.session_state.checked, on_click=utils.on_check)

    if st.session_state.checked:

        sentence = ' '.join(answer_list)

        result = utils.match(text=sentence, target=target)

        if result: 
            st.success('**Correcto!**')
        else:
            st.error('''
                     **Incorrecto!**  
                     {0}'''.format(utils.to_canon(target)))

        cols = st.columns((2,1), vertical_alignment='bottom')

        with cols[0]:
            st.empty()    
        
        with cols[1]:
            if st.button(label='Siguiente...', use_container_width=True, type='primary'):
                # CLEANUP
                del st.session_state.checked
                del st.session_state.pieces

                return result

    else:
        return None
