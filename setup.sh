mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"fpdll.cid20@uea.edu.br\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml