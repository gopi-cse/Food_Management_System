"""Project package.

PyMySQL is included as a beginner-friendly MySQL driver, especially for Windows
users who can have trouble compiling mysqlclient.
"""
try:
    import pymysql

    pymysql.install_as_MySQLdb()
except ImportError:
    pass
