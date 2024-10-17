import reflex as rx
import httpx
from ..states.question_state import QuestionState

def question_card_vertical(question_title: str, question_author: str, question_description: str,)-> rx.Component:

    return rx.card(
            rx.vstack(
                rx.heading(question_title),
                rx.text(f"Created by user {question_author}"),
                rx.divider(),
                rx.text(question_description),
                width="100%",
                spacing="5",
                align='start',
            ),
            as_child=True,
            width = "60vw",
            size="5",
            align='start',
        )

def question_grid_vertical()-> rx.Component:
    return rx.vstack(
        rx.cond(
            QuestionState.questions != [],
            rx.foreach(QuestionState.questions, lambda value, i: 
                        question_card_vertical(question_title = value["title"],
                                    question_author = value["created_by"],
                                    question_description = value["question"])),
            rx.text("No questions available")
        ),   
        spacing_y="4",
        #width="100%",
        align ="start",
        justify = "start"
    )
