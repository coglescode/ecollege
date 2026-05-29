
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

			// Nav Scroll Visual Transition Management
			window.addEventListener('scroll', handleScroll);
			function handleScroll() {
				if (window.scrollY > 50) {
					// Scrolled Down State (Frosted glass navigation panel)
					mainNav.classList.remove('bg-transparent', 'border-b', 'border-white/10', 'py-4', 'sm:py-5');
					mainNav.classList.add('bg-white/95', 'backdrop-blur-md', 'shadow-md', 'shadow-slate-200/40', 'border-b', 'border-slate-100', 'py-3');

					// Text visual color corrections
					document.getElementById('nav-brand-text').classList.replace('text-white', 'text-slate-900');
					document.getElementById('nav-login-btn').classList.replace('text-white/90', 'text-slate-600');
					document.getElementById('nav-login-btn').classList.replace('hover:text-white', 'hover:text-indigo-600');

					// Button style overrides
					//const ctaBtn = document.getElementById('nav-cta-btn');
					//ctaBtn.className = "bg-indigo-600 text-white px-6 py-2.5 rounded-xl font-bold hover:bg-indigo-700 transition shadow-lg shadow-indigo-100 text-sm";

					// Regular links color sync
					document.querySelectorAll('.nav-link').forEach(link => {
						link.classList.replace('text-white/90', 'text-slate-600');
						link.classList.replace('hover:text-white', 'hover:text-indigo-600');
					});

					// Adjust hamburger buttons
					document.getElementById('mobile-menu-btn').classList.replace('text-white', 'text-slate-800');
				} else {
					// Top Transparent State
					mainNav.classList.remove('bg-white/95', 'backdrop-blur-md', 'shadow-md', 'shadow-slate-200/40', 'border-b', 'border-slate-100', 'py-3');
					mainNav.classList.add('border-b', 'border-white/10', 'py-4', 'sm:py-5');

					document.getElementById('nav-brand-text').classList.replace('text-slate-900', 'text-white');
					document.getElementById('nav-login-btn').classList.replace('text-slate-600', 'text-white/90');
					document.getElementById('nav-login-btn').classList.replace('hover:text-indigo-600', 'hover:text-white');

					//const ctaBtn = document.getElementById('nav-cta-btn');
					//ctaBtn.className = "bg-white text-indigo-600 px-6 py-3 rounded-xl font-bold hover:bg-slate-100 transition shadow-lg shadow-black/10 text-sm";

					document.querySelectorAll('.nav-link').forEach(link => {
						link.classList.replace('text-slate-600', 'text-white/90');
						link.classList.replace('hover:text-indigo-600', 'hover:text-white');
					});

					document.getElementById('mobile-menu-btn').classList.replace('text-slate-800', 'text-white');
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


