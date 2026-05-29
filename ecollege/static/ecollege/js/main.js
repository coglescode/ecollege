
document.addEventListener('DOMContentLoaded', function() {

			// DOM Handles
			const mainNav = document.getElementById('main-nav');
			const desktopDropdown = document.getElementById('desktop-dropdown');
			const dropdownChevron = document.getElementById('dropdown-chevron');
			const mobileDrawer = document.getElementById('mobile-drawer');
			const mobileDrawerBackdrop = document.getElementById('mobile-drawer-backdrop');
			const mobileMenuBtn = document.getElementById('mobile-menu-btn');
			const mobileCloseBtn = document.getElementById('mobile-close-btn');

			const mobileAccordionContent = document.getElementById('mobile-accordion-content');
			const accordionChevron = document.getElementById('accordion-chevron');
			const hamburgerPath = document.getElementById('hamburger-path');
			const navBrandText = document.getElementById('nav-brand-text');

			// Nav Scroll Visual Transition Management
			window.addEventListener('scroll', handleScroll);
			function handleScroll() {
				const isScrolled = window.scrollY > 50;
				// === NAV BACKGROUND ===
				if (isScrolled) {
						mainNav.classList.remove( 'border-b', 'border-white/10', 'py-4', 'sm:py-5');
						mainNav.classList.add('bg-white/95', 'backdrop-blur-md', 'shadow-md', 'shadow-slate-200/40', 'border-b', 'border-slate-100', 'py-3');
				} else {
						mainNav.classList.remove('bg-white/95', 'backdrop-blur-md', 'shadow-md', 'shadow-slate-200/40', 'border-b', 'border-slate-100', 'py-3');
						mainNav.classList.add( 'border-b', 'border-white/10', 'py-4', 'sm:py-5');
				}

				// === BRAND TEXT ===
				const brandText = document.getElementById('nav-brand-text');
				if (brandText) {
						brandText.classList.toggle('text-slate-900', isScrolled);
						brandText.classList.toggle('text-white', !isScrolled);
				}

				// === ALL NAV LINKS (including authenticated versions) ===
				document.querySelectorAll('.nav-link').forEach(link => {
						if (isScrolled) {
								// Scrolled = Light mode
								link.classList.remove('text-white/90', 'hover:text-white');
								link.classList.add('text-slate-600', 'hover:text-indigo-600');
						} else {
								// Top = Transparent mode
								link.classList.remove('text-slate-600', 'hover:text-indigo-600');
								link.classList.add('text-white/90', 'hover:text-white');
						}
    		});

				// === HAMBURGER ===
				const mobileMenuBtnEl = document.getElementById('mobile-menu-btn');
				if (mobileMenuBtnEl) {
						mobileMenuBtnEl.classList.toggle('text-slate-800', isScrolled);
						mobileMenuBtnEl.classList.toggle('text-white', !isScrolled);
				}
			}

			// Desktop Dropdown Open/Close Mechanics
			let dropdownOpen = false;
			function toggleCategoriesDropdown(event) {
				event.stopPropagation();
				dropdownOpen = !dropdownOpen;

				if (dropdownOpen) {
					desktopDropdown.classList.remove('scale-95', 'opacity-0', 'pointer-events-none');
					desktopDropdown.classList.add('scale-100', 'opacity-100', 'pointer-events-auto');
					dropdownChevron.classList.add('rotate-180');
				} else {
					closeDesktopDropdown();
				}
			}

			function closeDesktopDropdown() {
				dropdownOpen = false;
				desktopDropdown.classList.add('scale-95', 'opacity-0', 'pointer-events-none');
				desktopDropdown.classList.remove('scale-100', 'opacity-100', 'pointer-events-auto');
				dropdownChevron.classList.remove('rotate-180');
			}

			// Mobile Sidebar Drawer Mechanics
			mobileMenuBtn.addEventListener('click', toggleMobileMenu)
			mobileDrawerBackdrop.addEventListener('click', toggleMobileMenu)
			mobileCloseBtn.addEventListener('click', toggleMobileMenu)

			let mobileMenuOpen = false;
			function toggleMobileMenu() {
				mobileMenuOpen = !mobileMenuOpen;

				if (mobileMenuOpen) {
					// Open mobile drawer with backdrop blur fade-in
					mobileDrawer.classList.remove('translate-x-full');
					mobileDrawer.classList.add('translate-x-0');

					mobileDrawerBackdrop.classList.remove('opacity-0', 'pointer-events-none');
					mobileDrawerBackdrop.classList.add('opacity-100', 'pointer-events-auto');

					// Animate hamburger to an "X" shape
					hamburgerPath.setAttribute('d', 'M6 18L18 6M6 6l12 12');

					// Prevent scrolling of underlying page content
					document.body.classList.add('overflow-hidden');
				} else {
					// Close mobile drawer
					mobileDrawer.classList.remove('translate-x-0');
					mobileDrawer.classList.add('translate-x-full');

					mobileDrawerBackdrop.classList.remove('opacity-100', 'pointer-events-auto');
					mobileDrawerBackdrop.classList.add('opacity-0', 'pointer-events-none');

					// Reset hamburger icon path
					hamburgerPath.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');

					// Allow scrolling again
					document.body.classList.remove('overflow-hidden');
				}
			}


			// Mobile Accordion (Dropdown inside drawer) Mechanics
			accordionChevron.addEventListener('click', toggleMobileAccordion);
			let accordionOpen = false;
			function toggleMobileAccordion() {
				accordionOpen = !accordionOpen;

				if (accordionOpen) {
					mobileAccordionContent.classList.remove('hidden');
					accordionChevron.classList.add('rotate-180');
				} else {
					mobileAccordionContent.classList.add('hidden');
					accordionChevron.classList.remove('rotate-180');
				}
			}


			// Anchor navigation scroll trigger
			function scrollToSubjects() {
				const el = document.getElementById('categories-section');
				if (el) el.scrollIntoView({ behavior: 'smooth' });
			}

			// Close dropdowns if clicking anywhere else on page
			document.addEventListener('click', () => {
				if (dropdownOpen) closeDesktopDropdown();
			});

			// Event hooks
			window.addEventListener('scroll', handleScroll);
			window.addEventListener('load', handleScroll);


	})


