--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: frank
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time integer,
    vote_number integer,
    question_id integer,
    message text,
    image text
);


ALTER TABLE public.answer OWNER TO frank;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: frank
--

CREATE SEQUENCE public.answer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO frank;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: frank
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: frank
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time integer,
    view_number text,
    vote_number text,
    title text,
    message text,
    image text
);


ALTER TABLE public.question OWNER TO frank;

--
-- Name: question_seq; Type: SEQUENCE; Schema: public; Owner: frank
--

CREATE SEQUENCE public.question_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_seq OWNER TO frank;

--
-- Name: question_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: frank
--

ALTER SEQUENCE public.question_seq OWNED BY public.question.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: frank
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: frank
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: frank
--

COPY public.answer (id, submission_time, vote_number, question_id, message, image) FROM stdin;
1	1493398154	4	1	You need to use brackets: my_list = []	\N
2	1493088154	35	1	Look it up in the Python docs	\N
4	1586592289	3	4	3 kezzel inserted	\N
8	1586592289	3	4	3 kezzel inserted	\N
9	1586592289	3	4	3 kezzel inserted	\N
10	1586592289	3	4	3 kezzel inserted	\N
11	1586592289	3	4	3 kezzel inserted	\N
12	1586592289	3	4	3 kezzel inserted	\N
13	1586592289	3	4	3 kezzel inserted	\N
14	1586592289	3	4	3 kezzel inserted	\N
15	1586592289	3	4	3 kezzel inserted	\N
16	1587286653	\N	4	wwwww one week later	\N
17	1587286690	\N	4	Another one 17 lesz?	\N
20	1587295735	\N	19	Whatever comment is, it's here.	\N
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: frank
--

COPY public.question (id, submission_time, view_number, vote_number, title, message, image) FROM stdin;
2	1586592285	2	3	kezzel inserted	kezzel inserted q	\N
3	1586592289	3	4	4 title of q	3 kezzel inserted	\N
8	1586592289	3	4	4 title of q	3 kezzel inserted	\N
12	1586592289	3	4	4 title of q	3 kezzel inserted	\N
10	1586592289	3	4	4 title of question 4	updated first Sunday	\N
4	1586592284	\N	\N	a volt, most mas a kerdes	a volt most ez is mas - tul sok valasz van erre???\r\nvajon?? nem??	\N
7	1586592285	2	3	Added from DataGrip	Manually added from Data Grip	\N
6	1586592285	2	3	entry from datagrip query	entry from query in datagrip???	\N
15	1587292877	\N	\N	Added question too late?	Added question too late?	\N
16	1587292906	\N	\N	New ques?	New question ??	\N
18	1587293010	\N	\N	questin number 17? esetleg?	Again, is it 17?	\N
19	1587295702	\N	\N	question no. 18? Neem?	Another new question 18?	\N
20	1587295782	\N	\N	question MESSAGE	Question TITLE	\N
21	1587295872	\N	\N	Q 21 TITLE	q 21 message	\N
\.


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: frank
--

SELECT pg_catalog.setval('public.answer_id_seq', 23, true);


--
-- Name: question_seq; Type: SEQUENCE SET; Schema: public; Owner: frank
--

SELECT pg_catalog.setval('public.question_seq', 21, true);


--
-- Name: answer answer_pk; Type: CONSTRAINT; Schema: public; Owner: frank
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_pk PRIMARY KEY (id);


--
-- Name: question question_pk; Type: CONSTRAINT; Schema: public; Owner: frank
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pk PRIMARY KEY (id);


--
-- Name: answer_id_uindex; Type: INDEX; Schema: public; Owner: frank
--

CREATE UNIQUE INDEX answer_id_uindex ON public.answer USING btree (id);


--
-- PostgreSQL database dump complete
--

