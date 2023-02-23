CREATE TABLE public.t_user
(
    userid uuid NOT NULL DEFAULT gen_random_uuid(),
    name character varying NOT NULL DEFAULT (''),
    username character varying NOT NULL DEFAULT (''),
    email character varying NOT NULL DEFAULT (''),
    password character varying NOT NULL DEFAULT (''),
    secretkey character varying NOT NULL DEFAULT (''),
    created timestamp NOT NULL DEFAULT now(),
    createby character varying,
    updated timestamp,
    updateby character varying,
    deleteflag integer NOT NULL DEFAULT 0,
    PRIMARY KEY (userid)
) TABLESPACE pg_default;

ALTER TABLE public.t_user
    OWNER to ducellesystem;
