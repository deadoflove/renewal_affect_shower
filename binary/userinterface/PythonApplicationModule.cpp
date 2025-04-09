// 1) Search: search at the end 

}

// 2) before its end make a new line and paste:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	PyModule_AddIntConstant(poModule, "ENABLE_RENEWAL_AFFECT_SHOWER", true);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_RENEWAL_AFFECT_SHOWER", false);
#endif


// Example:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	PyModule_AddIntConstant(poModule, "ENABLE_RENEWAL_AFFECT_SHOWER", true);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_RENEWAL_AFFECT_SHOWER", false);
#endif

}