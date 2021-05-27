import sqlite3
def execute_sql(sql):
    try:
        conn = sqlite3.connect("../data/Awd.db")
    except:
        conn = sqlite3.connect("./data/Awd.db")
    c = conn.cursor()
    try:
        result = c.execute(sql)
        conn.commit()
        # conn.close()
        return result
    except:
        return False
def select_ip():
    sql = """select ip from ipList;"""
    result = execute_sql(sql)
    return result

#插入flag
def insert_flag(ip,flag):
    sql = f"""insert into flagList(ip,flag)values('{ip}','{flag}');"""
    try:
        execute_sql(sql)
        return True
    except:
        return False
#清空flag
def init_flag():
    sql = "DELETE FROM flagList;"
    try:
        execute_sql(sql)
        return True
    except:
        return False
def init_ssh():
    sql = "DELETE FROM sshIp;"
    try:
        execute_sql(sql)
        return True
    except:
        return False
def init_softLink():
    sql = "DELETE FROM softLink;"
    try:
        execute_sql(sql)
        return True
    except:
        return False
def select_ssh():
    sql = """select ip from sshIp;"""
    result = execute_sql(sql)
    return result
def select_flag():
    sql = """select ip,flag from flagList;"""
    return execute_sql(sql)
def select_shell():
    sql = "select * from webshell;"
    return execute_sql(sql)
def select_behinder():
    sql = "select * from behinder;"
    return  execute_sql(sql)
def insert_softLink(ip,softLink):
    sql = f"""insert into softLink(ip,softLink)values('{ip}','{softLink}');"""
    return execute_sql(sql)
def select_softLink():
    sql = "select * from softLink;"
    return execute_sql(sql)

