from nicegui import ui
import os
from components.footer import show_footer
from components.navbar import show_navbar


def build_hero_section():
    with ui.element("div").style(
        "background-image:url(assets/hero.image.png)"
    ).classes("h-screen w-screen flex flex-col bg-no-repeat bg-cover bg-center m-0 p-0"):
        with ui.column().classes("items-center justify-center self-center text-center h-full w-full"):
            ui.label("Made For Those").classes("font-bold text-white uppercase").style("font-size:4rem;")
            ui.label("Who Do").classes("font-bold text-white uppercase").style("font-size:4rem;")


def build_search_card():
    with ui.element("div").classes("max-w-[1200px] mx-auto px-4 -mt-10 relative z-10"):
        with ui.row().classes("bg-[#1F1471] text-white rounded-xl p-4 shadow-xl gap-4 items-end flex-wrap"):
            with ui.column().classes("min-w-[220px] flex-1"):
                ui.label("Looking for").classes("text-xs text-white mb-1")
                ui.select({"conf": "Conference", "meet": "Meetup", "work": "Workshop"}, with_input=True, value=None)\
                    .props("placeholder=Choose event type dense")\
                    .classes("w-full bg-white text-black rounded-md h-10")

            with ui.column().classes("min-w-[220px] flex-1"):
                ui.label("Location").classes("text-xs text-white mb-1")
                ui.select({"nyc": "New York", "ldn": "London", "blr": "Bengaluru", "lag": "Lagos"}, with_input=True, value=None)\
                    .props("placeholder=Choose location dense")\
                    .classes("w-full bg-white text-black rounded-md h-10")

            with ui.column().classes("min-w-[220px] flex-1"):
                ui.label("When").classes("text-xs text-white mb-1")
                ui.select({"today": "Today", "tomorrow": "Tomorrow", "weekend": "This weekend"}, with_input=True, value=None)\
                    .props("placeholder=Choose date and time dense")\
                    .classes("w-full bg-white text-black rounded-md h-10")

            ui.button(icon="search", on_click=lambda: ui.notify("Searching events..."))\
                .classes("h-10 w-10 rounded-md flex items-center justify-center text-white")\
                .style("background:#7C4DFF;")


def build_upcoming_section():
    with ui.element("div").classes("max-w-[1200px] mx-auto px-4 mt-6"):
        with ui.row().classes("items-center justify-between"):
            with ui.row().classes("items-baseline gap-2"):
                ui.label("Upcoming").classes("text-lg font-bold")
                ui.label("Events").classes("text-lg font-bold").style("color:#7C4DFF")
            with ui.row().classes("gap-2"):
                ui.select({"wd": "Weekdays", "we": "Weekends"}, value="wd")
                ui.select({"all": "Event type", "conf": "Conference", "meet": "Meetup", "work": "Workshop"}, value="all")
                ui.select({"any": "Any category", "tech": "Tech", "biz": "Business", "edu": "Education"}, value="any")

        def event_card(img: str, title: str, date_str: str, place: str):
            with ui.element("div").classes("bg-white rounded-xl border border-gray-200 shadow-md overflow-hidden"):
                with ui.element("div").classes("relative p-2 pt-2"):
                    ui.image(img).classes("w-full h-44 object-cover rounded-lg")
                    ui.element("span").classes("absolute top-4 left-4 bg-white font-bold text-xs px-3 py-1 rounded-md shadow text-[#7C4DFF]").text = "FREE"
                with ui.element("div").classes("p-4"):
                    ui.label(title).classes("text-base font-semibold")
                    ui.link(date_str, "#").classes("text-sm").style("color:#7C4DFF")
                    try:
                        fixed_place = place.replace("A�", "·")
                    except Exception:
                        fixed_place = place
                    ui.label(fixed_place).classes("text-xs text-gray-500")

        with ui.element("div").classes("grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-2"):
            event_card("https://images.unsplash.com/photo-1542773665-98aef53b39b3?q=80&w=1200&auto=format&fit=crop", "BestSeller Book Bootcamp - write, Market & Publish Your Book - Lucknow", "Saturday, March 18, 3:00PM", "ONLINE EVENT · Attend anywhere")
            event_card("https://images.unsplash.com/photo-1531058020387-3be344556be6?q=80&w=1200&auto=format&fit=crop", "BestSeller Book Bootcamp - write, Market & Publish Your Book - Lucknow", "Saturday, March 18, 3:00PM", "ONLINE EVENT · Attend anywhere")
            event_card("https://images.unsplash.com/photo-1515165562835-c3b8c1ea39f2?q=80&w=1200&auto=format&fit=crop", "BestSeller Book Bootcamp - write, Market & Publish Your Book - Lucknow", "Saturday, March 18, 3:00PM", "ONLINE EVENT · Attend anywhere")
            event_card("https://images.unsplash.com/photo-1492684223066-81342ee5ff30?q=80&w=1200&auto=format&fit=crop", "BestSeller Book Bootcamp - write, Market & Publish Your Book - Lucknow", "Saturday, March 18, 3:00PM", "ONLINE EVENT · Attend anywhere")
            event_card("https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1200&auto=format&fit=crop", "BestSeller Book Bootcamp - write, Market & Publish Your Book - Lucknow", "Saturday, March 18, 3:00PM", "ONLINE EVENT · Attend anywhere")
            event_card("https://images.unsplash.com/photo-1519345182560-3f2917c472ef?q=80&w=1200&auto=format&fit=crop", "BestSeller Book Bootcamp - write, Market & Publish Your Book - Lucknow", "Saturday, March 18, 3:00PM", "ONLINE EVENT · Attend anywhere")

        with ui.row().classes("justify-center mt-3"):
            ui.button("Load more...", on_click=lambda: ui.notify("Load more"))\
                .classes("h-10 rounded-md px-5 text-white").style("background: linear-gradient(180deg, #7C4DFF, #5A2EE5);")


def build_cta_banner():
    with ui.element("div").classes("max-w-[1200px] mx-auto px-4 my-6"):
        with ui.row().classes("rounded-xl text-white overflow-hidden items-center gap-4 p-5")\
            .style("background: linear-gradient(90deg, #1F1471 0%, #4D2FE2 60%);"):
            with ui.element("div").classes("flex items-center justify-center"):
                # Prefer your local vector.people.png; fallback to cta_illustration.png; then remote
                cta_local_vec = "assets/vector.people.png"
                cta_local_alt = "assets/cta_illustration.png"
                if os.path.isfile(cta_local_vec):
                    cta_src = f"/assets/{os.path.basename(cta_local_vec)}"
                elif os.path.isfile(cta_local_alt):
                    cta_src = f"/assets/{os.path.basename(cta_local_alt)}"
                else:
                    cta_src = "https://raw.githubusercontent.com/typicaljoe/camper-logo-assets/master/illustrations/couch_couple.png"
                ui.image(cta_src).classes("w-[300px] h-[160px] object-contain")
            with ui.column().classes("gap-2"):
                ui.label("Make your own Event").classes("text-2xl font-extrabold")
                ui.label("Lorem ipsum dolor sit amet, consectetur adipiscing elit.").classes("text-sm opacity-90")
                ui.button("Create Events", on_click=lambda: ui.navigate.to("/create_event")).classes("h-10 w-48 rounded-md text-white")\
                    .style("background: linear-gradient(180deg, #7C4DFF, #5A2EE5);")


def build_asset_divider():
    """Full‑width decorative divider using an image from assets.

    If the provided image exists in `assets/`, it will be repeated horizontally
    to span the full page width. Otherwise, this section is skipped silently.
    """
    local = "assets/2e076d64385642e5d482db14204739d55ac435fa.png"
    if os.path.isfile(local):
        # full‑bleed strip
        with ui.element("div").style(
            'width:100vw; margin-left:calc(50% - 50vw); height:18px; '
            f'background: url("/assets/{os.path.basename(local)}") repeat-x center/auto 18px;'
        ):
            pass


def build_brands_strip():
    with ui.column().classes("max-w-[1200px] mx-auto px-4 my-6 gap-2"):
        # Header
        with ui.row().classes("items-baseline justify-center"):
            ui.label("Join these").classes("text-lg font-bold")
            ui.label("brands").classes("text-lg font-bold").style("color:#7C4DFF; margin-left:6px;")
        # Boxed container around logos (per screenshot)
        with ui.element("div").classes("bg-white rounded-xl border-2 border-gray-300 p-6"):
            ui.label("We've had the pleasure of working with industry-defining brands. These are just some of them.")\
                .classes("text-sm text-center text-gray-600 mb-4")
            with ui.row().classes("gap-8 flex-wrap items-center justify-center"):
                # Use only local assets (no remote fallbacks)
                logos = [
                    ("spotify.png", "Spotify"),
                    ("google.png", "Google"),
                    ("stripe.png", "Stripe"),
                    ("youtube.png", "YouTube"),
                    ("microsoft.png", "Microsoft"),
                    ("medium.png", "Medium"),
                    ("zoom.png", "Zoom"),
                    ("uber.png", "Uber"),
                    ("grab.png", "Grab"),
                ]
                for local, alt in logos:
                    ui.image(f"/assets/{local}").props("alt="+alt).style("height:40px; width:auto; object-fit:contain;")


def build_trending_section():
    with ui.column().classes("max-w-[1200px] mx-auto px-4 mt-4 gap-2"):
        with ui.row().classes("items-baseline gap-2"):
            ui.label("Trending").classes("text-lg font-bold")
            ui.label("colleges").classes("text-lg font-bold").style("color:#7C4DFF")

        with ui.element("div").classes("grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"):
            cards = [
                ("https://images.unsplash.com/photo-1588072432836-e10032774350?q=80&w=1200&auto=format&fit=crop", "Harvard University", "Cambridge, Massachusetts, US"),
                ("https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1200&auto=format&fit=crop", "Stanford University", "Stanford, California"),
                ("https://images.unsplash.com/photo-1536412597336-ade7d510f3d7?q=80&w=1200&auto=format&fit=crop", "Nanyang University", "Nanyang Ave, Singapore"),
            ]
            for img, title, meta in cards:
                with ui.element("div").classes("bg-white rounded-xl border border-gray-200 shadow-md overflow-hidden"):
                    ui.image(img).classes("w-full h-44 object-cover")
                    with ui.element("div").classes("p-4"):
                        ui.label(title).classes("text-base font-semibold")
                        ui.label(meta).classes("text-sm text-gray-600")

        with ui.row().classes("justify-center mt-3"):
            ui.button("Load more...", on_click=lambda: ui.notify("More colleges"))\
                .classes("h-10 rounded-md px-5 text-white").style("background: linear-gradient(180deg, #7C4DFF, #5A2EE5);")


def build_blog_section():
    with ui.column().classes("max-w-[1200px] mx-auto px-4 mt-6 mb-3 gap-2"):
        with ui.row().classes("items-baseline gap-2"):
            ui.label("Our").classes("text-lg font-bold")
            ui.label("Blogs").classes("text-lg font-bold").style("color:#7C4DFF")

        with ui.element("div").classes("grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"):
            posts = [
                ("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1200&auto=format&fit=crop", "Behind the scenes of EventHive", "3 min read"),
                ("https://images.unsplash.com/photo-1513546493312-0066d7de3fd2?q=80&w=1200&auto=format&fit=crop", "How to host your first meetup", "6 min read"),
                ("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=1200&auto=format&fit=crop", "Design that delights attendees", "5 min read"),
            ]
            for img, title, meta in posts:
                with ui.element("div").classes("bg-white rounded-xl border border-gray-200 shadow-md overflow-hidden"):
                    ui.image(img).classes("w-full h-40 object-cover")
                    with ui.element("div").classes("p-3"):
                        ui.label(title).classes("text-base font-semibold")
                        ui.label(meta).classes("text-sm text-gray-600")
        with ui.row().classes("justify-center mt-3"):
            ui.button("View all", on_click=lambda: ui.notify("View all blogs"))\
                .classes("h-10 rounded-md px-5 text-white").style("background: linear-gradient(180deg, #7C4DFF, #5A2EE5);")


def build_newsletter_section():
    with ui.element("div").classes("max-w-[1200px] mx-auto px-4 my-8"):
        with ui.row().classes("bg-white rounded-xl shadow-lg items-center justify-between flex-wrap gap-3 p-4"):
            with ui.column().classes("min-w-[260px] gap-1"):
                ui.label("Stay in the loop").classes("text-lg font-bold")
                ui.label("Get updates on new events, perks and more").classes("text-sm text-gray-500")
            with ui.row().classes("items-center gap-2"):
                email = ui.input(placeholder="Enter your email").props("type=email aria-label=Email").classes("rounded-md h-10 min-w-[220px]")
                ui.button("Subscribe", on_click=lambda: ui.notify(f"Subscribed: {email.value or ''}"))\
                    .classes("h-10 rounded-md px-4 text-white").style("background:#7C4DFF")


@ui.page("/")
def show_home_page():
    show_navbar()
    build_hero_section()
    build_search_card()
    build_asset_divider()
    build_upcoming_section()
    build_cta_banner()
    build_brands_strip()
    build_trending_section()
    build_blog_section()
    build_newsletter_section()
    show_footer()
