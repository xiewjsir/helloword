#!/usr/bin/env pythone3
# -*- coding:utf-8 -*-

from sqlalchemy import Column,String,create_engine

engine = create_engine('mysql+mysqlconnector://root@localhost:3306/spider')

print(engine)