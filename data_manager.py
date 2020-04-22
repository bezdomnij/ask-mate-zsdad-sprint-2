from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor
import database_common


@database_common.connection_handler
def get_questions(cursor: RealDictCursor) -> list:
    query = """
        SELECT *
        FROM question
        ORDER BY submission_time"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_vote_number(cursor: RealDictCursor, q_id:int) -> list:
    query = """
        SELECT vote_number
        FROM question
        WHERE id = %(q_id)s"""
    cursor.execute(query, {'q_id': q_id})
    return cursor.fetchall()


@database_common.connection_handler
def write_vote_number(cursor: RealDictCursor, q_id:int, v_number) -> list:
    query = """
        UPDATE question SET vote_number = %(vote_number)s
        WHERE id = %(q_id)s"""
    cursor.execute(query, {'vote_number': v_number, 'q_id': q_id})


@database_common.connection_handler
def get_question_by_id(cursor: RealDictCursor, question_id):
    query = """
        SELECT * FROM question WHERE id = %(qid)s;"""
    cursor.execute(query, {'qid': question_id})
    return cursor.fetchone()


@database_common.connection_handler
def get_answers(cursor: RealDictCursor) -> list:
    query = """
        SELECT *
        FROM answer
        ORDER BY id;"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_answer_by_question_id(cursor: RealDictCursor, question_id):
    query = """
        SELECT * FROM answer WHERE question_id = %(qid)s;"""
    cursor.execute(query, {'qid': question_id})
    return cursor.fetchall()


@database_common.connection_handler
def add_answer(cursor: RealDictCursor, answer_details):
    query = """
        INSERT INTO answer  (submission_time, vote_number, question_id, message)
        VALUES(%(s_t)s, %(v_n)s, %(q_i)s, %(m_g)s);"""
    cursor.execute(query, {
        's_t': answer_details['submission_time'],
        'v_n': answer_details['vote_number'],
        'q_i': answer_details['question_id'],
        'm_g': answer_details['message']
    })
    return


@database_common.connection_handler
def delete_question(cursor: RealDictCursor, qid: int):
    query = """
        DELETE FROM question WHERE id = %(qid)s;"""
    cursor.execute(query, {'qid': qid})
    return


@database_common.connection_handler
def delete_answer(cursor: RealDictCursor, question_id: int):
    query = """
        DELETE FROM answer WHERE question_id = %(q_id)s;"""
    cursor.execute(query, {'q_id': question_id})
    return


@database_common.connection_handler
def update_question(cursor: RealDictCursor, question_id: int, message: str, title: str):
    query = """
        UPDATE question 
        SET title = %(tt)s, message = %(msg)s
        WHERE id = %(qid)s;"""
    cursor.execute(query, {'tt': title, 'msg': message, 'qid': question_id})
    return


@database_common.connection_handler
def insert_question(cursor: RealDictCursor, question: dict):
    query = """
        INSERT INTO question (submission_time, title, message, vote_number, view_number)
        VALUES (%(st)s, %(ttl)s, %(msg)s, %(vo_n)s, %(vi_n)s);"""
    cursor.execute(query, {
        'st': question['submission_time'],
        'msg': question['message'],
        'ttl': question['title'],
        'vo_n': question['vote_number'],
        'vi_n': question['view_number']
    })
    return


@database_common.connection_handler
def delete_answer_by_id(cursor: RealDictCursor, answer_id: int):
    query = """
        DELETE FROM answer WHERE id = %(aid)s;"""
    cursor.execute(query, {'aid': answer_id})
    return


@database_common.connection_handler
def write_comment_to_question(cursor: RealDictCursor, q_id, s_time, ct):
    query = """
    INSERT INTO comment(question_id, submission_time, message)
    VALUES (%(q_id)s, %(s_time)s, %(ct)s);"""
    cursor.execute(query, {'q_id': q_id, 's_time': s_time, 'ct': ct})

@database_common.connection_handler
def get_question_comments(cursor: RealDictCursor, qid) -> list:
    query = """
        SELECT *
        FROM comment WHERE question_id = %(qid)s
        ORDER BY submission_time"""
    cursor.execute(query, {'qid': qid})
    return cursor.fetchall()

@database_common.connection_handler
def get_answer_comments(cursor: RealDictCursor) -> list:
    query = """
        SELECT *
        FROM comment WHERE answer_id is not null
        ORDER BY submission_time"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def write_comment_to_answer(cursor: RealDictCursor, a_id, s_time, ct):
    query = """
    INSERT INTO comment(answer_id, submission_time, message)
    VALUES (%(a_id)s, %(s_time)s, %(ct)s);"""
    cursor.execute(query, {'a_id': a_id, 's_time': s_time, 'ct': ct})


@database_common.connection_handler
def get_latest_questions(cursor: RealDictCursor) -> list:
    query = """
        SELECT *
        FROM question
        ORDER BY submission_time DESC LIMIT 5"""
    cursor.execute(query)
    return cursor.fetchall()