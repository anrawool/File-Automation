from Controllers import server_conn

conn = server_conn.SSH_Connection('abhijitrawool', '192.168.1.13', 'sarthak09')
conn.exec_command("cd ~/StatupScripts && sh backup_script.sh")