from streamlit.testing.v1 import AppTest

from planner import build_plan


def test_rules_produce_distinct_surface_aware_plans():
    glass = build_plan("Glass or glazed ceramic", "Paper label", "Old or unknown", "Protect the item")
    wood = build_plan("Finished wood", "Plastic film or tape", "Fresh (under a week)", "Finish sooner")
    assert glass != wood
    assert any("wet cloth" in step for step in glass["steps"])
    assert any("with the grain" in step for step in wood["steps"])
    assert "color transfer" in wood["stop"]
    assert glass["first_action"]


def test_app_launches_with_title_controls_about_and_privacy():
    app = AppTest.from_file("streamlit_app.py").run()
    assert not app.exception
    assert app.title[0].value == "Stuck Label Rescue"
    assert len(app.selectbox) == 1
    assert len(app.radio) == 3
    assert app.button[0].label == "Build my removal plan"
    assert any(exp.label == "About this tool" for exp in app.expander)
    assert "Privacy:" in app.expander[0].caption[0].value


def test_choices_change_output_and_reset_clears_result():
    app = AppTest.from_file("streamlit_app.py").run()
    app.selectbox[0].select("Glass or glazed ceramic")
    app.radio[0].set_value("Paper label")
    app.radio[1].set_value("Old or unknown")
    app.button[0].click().run()
    glass_output = " ".join(item.value for item in app.markdown)
    assert "warm, wet cloth" in glass_output
    assert app.success and "Do this now" in app.success[0].value

    app.button[1].click().run()
    assert not app.success

    app.selectbox[0].select("Finished wood")
    app.radio[0].set_value("Plastic film or tape")
    app.radio[1].set_value("Fresh (under a week)")
    app.button[0].click().run()
    wood_output = " ".join(item.value for item in app.markdown)
    assert "with the grain" in wood_output
    assert wood_output != glass_output
