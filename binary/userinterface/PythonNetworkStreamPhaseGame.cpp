// Search:
void CPythonNetworkStream::__RefreshEquipmentWindow()
{
	m_isRefreshEquipmentWnd=true;
}

// paste below:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
void CPythonNetworkStream::__RefreshAffectWindow()
{
	m_isRefreshAffectWindow = true;
}
#endif

// Search:
	if (m_isRefreshGuildWndGradePage)
	{
		m_isRefreshGuildWndGradePage=false;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildGradePage", Py_BuildValue("()"));
		s_nextRefreshTime = curTime + 300;
	}

// Add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	if (m_isRefreshAffectWindow)
	{
		m_isRefreshAffectWindow = false;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshAffectWindow", Py_BuildValue("()"));
		s_nextRefreshTime = curTime + 300;
	}
#endif

// Search:
	m_isRefreshGuildWndGradePage=false;

// Add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	m_isRefreshAffectWindow = false;
#endif

// Search:
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_NEW_AddAffect", Py_BuildValue("(iiii)", rkElement.dwType, rkElement.bPointIdxApplyOn, rkElement.lApplyValue, rkElement.lDuration));

// Add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	__RefreshAffectWindow();
#endif

// Search:
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_NEW_RemoveAffect", Py_BuildValue("(ii)", kAffectRemove.dwType, kAffectRemove.bApplyOn));

// Add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	__RefreshAffectWindow();
#endif
