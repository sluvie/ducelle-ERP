CREATE TABLE public.t_employee
(
    employeeid uuid NOT NULL DEFAULT gen_random_uuid(),
    firstname character varying NOT NULL DEFAULT (''),
    middlename character varying NOT NULL DEFAULT (''),
    lastname character varying NOT NULL DEFAULT (''),
    birthname character varying NOT NULL DEFAULT (''),
    salutation character varying NOT NULL DEFAULT (''),
    alias character varying NOT NULL DEFAULT (''),
    prenametitle character varying NOT NULL DEFAULT (''),
    postnametitle character varying NOT NULL DEFAULT (''),
    citizenshipid uuid NOT NULL DEFAULT (''), -- lov to t_citizen
    socialinsurancenumber character varying NOT NULL DEFAULT (''),
    socialinsurancejoindate timestamp NOT NULL,
    gender int NOT NULL DEFAULT (0), -- lov to t_setting
    maritalstatus INT NOT NULL DEFAULT (0), -- lov to t_setting
    religion INT NOT NULL DEFAULT (0), -- lov to t_setting
    bloodtype INT NOT NULL DEFAULT (0), -- lov to t_setting
    placeofbirth character varying NOT NULL DEFAULT (''),
    dateofbirth timestamp NOT NULL DEFAULT('1900-01-01'),
    userid character varying NOT NULL DEFAULT (''),
    personid character varying NOT NULL DEFAULT (''),
    secretkey character varying NOT NULL DEFAULT (''),
    created timestamp NOT NULL DEFAULT now(),
    createby character varying,
    updated timestamp,
    updateby character varying,
    deleteflag integer NOT NULL DEFAULT 0,
    PRIMARY KEY (employeeid)
) TABLESPACE pg_default;

ALTER TABLE public.t_employee
    OWNER to ducellehr;
