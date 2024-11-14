# import pathlib
# import shutil

# from bs4 import BeautifulSoup
import streamlit as st

# def inject_ga():
#     GA_ID = "google_adsense"
#     GA_META = '<meta name="google-adsense-account" content="ca-pub-xxxxxxxxxxxx9488">'

#     # Insert the script in the head tag of the static template inside your virtual
#     index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
#     # logging.info(f'editing {index_path}')
#     soup = BeautifulSoup(index_path.read_text(), features="html.parser")
#     if not soup.find(id=GA_ID): 
#         bck_index = index_path.with_suffix('.bck')
#         if bck_index.exists():
#             shutil.copy(bck_index, index_path)  # FAIL PermissionDenied
#         else:
#             shutil.copy(index_path, bck_index)  # FAIL PermissionDenied
#         html = str(soup)
#         new_html = html.replace('<head>', '<head>\n' + GA_META)
#         index_path.write_text(new_html)  # FAIL PermissionDenied

# inject_ga()

st.set_page_config(page_title="HitzON", layout="wide", page_icon="random")

pages = [
    st.Page(page='app/login.py', title='Login'),
    st.Page(page='app/course.py', title='Curso'),
    st.Page(page='app/ranking.py', title='Ranking'),
    st.Page(page='app/shop.py', title='Tienda'),
    st.Page(page='app/ad.py', title='Ad')
    ]
pg = st.navigation(pages=pages)
pg.run()
