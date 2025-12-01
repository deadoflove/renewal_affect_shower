// search

struct command_info cmd_info[] =

// add to top

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
ACMD(do_remove_affect);
#endif

// search

	{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}

// add to top

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	{ "remove_affect",	do_remove_affect,		0,		POS_DEAD,	GM_PLAYER },
#endif