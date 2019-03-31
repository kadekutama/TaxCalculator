--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

-- Started on 2019-03-27 09:50:13

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 199 (class 1259 OID 16583)
-- Name: Product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Product" (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    price real NOT NULL,
    tax_code integer NOT NULL
);


ALTER TABLE public."Product" OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16581)
-- Name: Product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Product_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Product_id_seq" OWNER TO postgres;

--
-- TOC entry 2828 (class 0 OID 0)
-- Dependencies: 198
-- Name: Product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Product_id_seq" OWNED BY public."Product".id;


--
-- TOC entry 197 (class 1259 OID 16575)
-- Name: TaxCode; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."TaxCode" (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    refundable boolean NOT NULL
);


ALTER TABLE public."TaxCode" OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16573)
-- Name: TaxCode_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."TaxCode_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."TaxCode_id_seq" OWNER TO postgres;

--
-- TOC entry 2829 (class 0 OID 0)
-- Dependencies: 196
-- Name: TaxCode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."TaxCode_id_seq" OWNED BY public."TaxCode".id;


--
-- TOC entry 2692 (class 2604 OID 16586)
-- Name: Product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Product" ALTER COLUMN id SET DEFAULT nextval('public."Product_id_seq"'::regclass);


--
-- TOC entry 2691 (class 2604 OID 16578)
-- Name: TaxCode id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TaxCode" ALTER COLUMN id SET DEFAULT nextval('public."TaxCode_id_seq"'::regclass);


--
-- TOC entry 2822 (class 0 OID 16583)
-- Dependencies: 199
-- Data for Name: Product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Product" (id, name, price, tax_code) FROM stdin;
1	Lucky Stretch	1000	2
2	Big Mac	1000	1
3	Movie	150	3
\.


--
-- TOC entry 2820 (class 0 OID 16575)
-- Dependencies: 197
-- Data for Name: TaxCode; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."TaxCode" (id, name, refundable) FROM stdin;
1	Food & Beverage	t
2	Tobacco	f
3	Entertainment	f
\.


--
-- TOC entry 2830 (class 0 OID 0)
-- Dependencies: 198
-- Name: Product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Product_id_seq"', 3, true);


--
-- TOC entry 2831 (class 0 OID 0)
-- Dependencies: 196
-- Name: TaxCode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."TaxCode_id_seq"', 3, true);


--
-- TOC entry 2696 (class 2606 OID 16588)
-- Name: Product Product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_pkey" PRIMARY KEY (id);


--
-- TOC entry 2694 (class 2606 OID 16580)
-- Name: TaxCode TaxCode_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TaxCode"
    ADD CONSTRAINT "TaxCode_pkey" PRIMARY KEY (id);


--
-- TOC entry 2697 (class 2606 OID 16589)
-- Name: Product tax; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT tax FOREIGN KEY (tax_code) REFERENCES public."TaxCode"(id);


-- Completed on 2019-03-27 09:50:13

--
-- PostgreSQL database dump complete
--

