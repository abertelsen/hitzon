from sqlalchemy import text
import streamlit as st

conn = st.connection('turso', type='sql')

# records = conn.query('SELECT * FROM users')
# print(records)

username = 'abertelsen'
records = conn.query(f'SELECT name, nextlesson FROM users WHERE name="{username}" LIMIT 1', ttl=0)
print(records.iloc[0].to_dict())

for level in ['A2', 'A1']:
    username = 'abertelsen'
    nextlesson = '{0}.00.00.00'.format(level)
    print('nextlesson: {0}'.format(nextlesson))
    with conn.session as session:
        result = session.execute(text('UPDATE users SET nextlesson = :n WHERE name = :u ;'),
                        params={"n": nextlesson, "u": username})
        # print(result.all())
        session.commit()

    records = conn.query(f'SELECT name, nextlesson FROM users WHERE name="{username}" LIMIT 1', ttl=0)
    print(records.iloc[0].to_dict())
