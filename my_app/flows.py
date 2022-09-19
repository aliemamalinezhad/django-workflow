from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend

import random

from .models import  Person
from .views import get_persons

# @frontend.register
# class SampleFlow(Flow):
#     start = flow.Start(get_persons).Next(this.task)

#     task = flow.Handler(this.perform_task).Next(this.check_status)

#     check_status = flow.If(this.is_completed).Then(this.end).Else(this.task)

#     end = flow.End()

#     def perform_task(self, activation):
#         print('Perform task')
#         activation.process.completed = random.randint(0, 1)

#     def is_completed(self, activation):
#         print('Perform task')

#         return activation.process.completed

@frontend.register
class FirstFlow(Flow):
    process_class = Person


    start = (
        flow.Start(
            CreateProcessView,
            fields=["name", "last_name"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.my_request
        ).Next(this.end)
    )

    end = flow.End()

    def my_request(self, activation):
        print(activation.process.name)