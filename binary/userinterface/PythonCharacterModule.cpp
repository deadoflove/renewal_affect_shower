// 1) Search:

	PyModule_AddIntConstant(poModule, "AFFECT_RAMADAN_RING",				CInstanceBase::AFFECT_RAMADAN_RING);
#ifdef ENABLE_WOLFMAN_CHARACTER
	PyModule_AddIntConstant(poModule, "AFFECT_BLEEDING",					CInstanceBase::AFFECT_BLEEDING);
	PyModule_AddIntConstant(poModule, "AFFECT_RED_POSSESSION",				CInstanceBase::AFFECT_RED_POSSESSION);
	PyModule_AddIntConstant(poModule, "AFFECT_BLUE_POSSESSION",				CInstanceBase::AFFECT_BLUE_POSSESSION);
#endif

// 2) Add:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_POLYMORPH",				CInstanceBase::NEW_AFFECT_POLYMORPH);
#endif

