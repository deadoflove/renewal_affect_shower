// Search:

void initPlayer()

// add to top:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
PyObject * playerSkillIndexToAffectIndex(PyObject* poSelf, PyObject* poArgs)
{
	int dwSkillIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &dwSkillIndex))
		return Py_BuildException();

	DWORD iAffectIndex;
	if (!CPythonPlayer::Instance().SkillIndexToAffectIndex(dwSkillIndex, &iAffectIndex))
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", iAffectIndex);
}
#endif

// If you use any system to hide or show the affects, you can use this.

//replaces

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
PyObject * playerShowAffectShower(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer::Instance().ShowAffectShower();
	return Py_BuildNone();
}

PyObject * playerHideAffectShower(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer::Instance().HideAffectShower();
	return Py_BuildNone();
}

PyObject * playerSkillIndexToAffectIndex(PyObject* poSelf, PyObject* poArgs)
{
	int dwSkillIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &dwSkillIndex))
		return Py_BuildException();

	DWORD iAffectIndex;
	if (!CPythonPlayer::Instance().SkillIndexToAffectIndex(dwSkillIndex, &iAffectIndex))
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", iAffectIndex);
}
#endif

// Search:

		{ NULL,							NULL,								NULL },

// add to top:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		{ "SkillIndexToAffectIndex",	playerSkillIndexToAffectIndex,		METH_VARARGS },
#endif

// If you use any system to hide or show the affects, you can use this.

//replaces

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		{ "ShowAffectShower",			playerShowAffectShower,				METH_VARARGS },
		{ "HideAffectShower",			playerHideAffectShower,				METH_VARARGS },
		{ "SkillIndexToAffectIndex",	playerSkillIndexToAffectIndex,		METH_VARARGS },
#endif

// search
PyModule_AddIntConstant(poModule, "DS_SUB_HEADER_DO_REFINE",	DS_SUB_HEADER_DO_REFINE);

//add

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	PyModule_AddIntConstant(poModule, "RESIST_MAGIC",			POINT_RESIST_MAGIC);
#endif