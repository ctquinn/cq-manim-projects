from manim import *


class FineTuningYOLO(Scene):
    def construct(self):
        # Title
        title = Text("Fine-Tuning YOLO").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Pretrained Model
        pretrained_image_path = "media/supporting_images/base_yolo.png"
        pretrained_model = ImageMobject(pretrained_image_path).scale(0.2)
        pretrained_text = Text("Pre-trained YOLO Model", font_size=20).next_to(
            pretrained_model, DOWN
        )
        pretrained_group = Group(pretrained_model, pretrained_text)
        pretrained_group.move_to(LEFT * 4 + UP * 1.5)

        # Dataset
        dataset_image_path = (
            "media/supporting_images/football_training.png"  # Path to your image file
        )
        dataset_task = ImageMobject(dataset_image_path).scale(
            0.2
        )  # Adjust scale as needed
        dataset_text = Text("Labeled Dataset", font_size=20).next_to(dataset_task, DOWN)
        dataset_group = Group(dataset_task, dataset_text)
        dataset_group.move_to(LEFT * 4 + DOWN * 1.5)

        # Fine-Tuned Model
        fine_tuned_model_image_path = "media/supporting_images/fine_tuned_yolo.png"
        fine_tuned_model = ImageMobject(fine_tuned_model_image_path).scale(0.2)
        fine_tuned_text = Text("Fine-Tuned YOLO Model", font_size=20).next_to(
            fine_tuned_model, DOWN
        )
        fine_tuned_group = Group(fine_tuned_model, fine_tuned_text)
        fine_tuned_group.move_to(ORIGIN)

        # YOLO Task (Custom Image)
        yolo_image_path = (
            "media/supporting_images/football_yolo.png"  # Path to your image file
        )
        yolo_task = ImageMobject(yolo_image_path).scale(0.2)  # Adjust scale as needed
        yolo_task_text = Text("Specialized Object Detection", font_size=20).next_to(
            yolo_task, DOWN
        )
        yolo_task_group = Group(
            yolo_task, yolo_task_text
        )  # Use Group instead of VGroup
        yolo_task_group.move_to(RIGHT * 4)

        # Arrows
        arrow_pretrained_to_finetuned = Arrow(
            pretrained_group.get_right(), fine_tuned_group.get_left(), buff=0.5
        )
        arrow_dataset_to_finetuned = Arrow(
            dataset_group.get_right(), fine_tuned_group.get_left(), buff=0.5
        )
        arrow_finetuned_to_task = Arrow(
            fine_tuned_group.get_right(), yolo_task_group.get_left(), buff=0.5
        )

        # Animations
        self.play(FadeIn(pretrained_model), Write(pretrained_text))
        self.play(FadeIn(dataset_task), Write(dataset_text))
        self.wait(2)
        self.play(Create(arrow_pretrained_to_finetuned))
        self.play(Create(arrow_dataset_to_finetuned))
        self.wait(2)
        self.play(FadeIn(fine_tuned_model), Write(fine_tuned_text))
        self.wait(2)
        self.play(Create(arrow_finetuned_to_task))
        self.play(FadeIn(yolo_task), Write(yolo_task_text))
        self.wait(2)

        # End Scene
        self.play(FadeOut(Group(*self.mobjects)))
