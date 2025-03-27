{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import psycopg2\n",
    "\n",
    "class PGDatabase:\n",
    "    def __init__(self, host, database, user, password):\n",
    "        self.host = host\n",
    "        self.database = database\n",
    "        self.user = user\n",
    "        self.password = password\n",
    "        self.connection = psycopg2.connect(\n",
    "            host = host,\n",
    "            user = user,\n",
    "            password = password,\n",
    "            database = database,\n",
    "        )\n",
    "\n",
    "        self.cursor = self.connection.cursor()\n",
    "        self.connection.autocommit = True\n",
    "\n",
    "    def post(self, query, *args):\n",
    "        try:\n",
    "            self.cursor.execute(query, args)\n",
    "        except Exception as err:\n",
    "            raise print(repr(err))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
