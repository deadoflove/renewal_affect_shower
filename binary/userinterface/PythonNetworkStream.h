// Search:
		void __RefreshMallWindow();

// add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		void __RefreshAffectWindow();
#endif

// Search:
		bool m_isRefreshGuildWndGradePage;

// Add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		bool m_isRefreshAffectWindow;
#endif
