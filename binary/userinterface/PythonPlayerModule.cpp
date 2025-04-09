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

// Search:

		{ NULL,							NULL,								NULL },

// add to top:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		{ "SkillIndexToAffectIndex",	playerSkillIndexToAffectIndex,		METH_VARARGS },
#endif