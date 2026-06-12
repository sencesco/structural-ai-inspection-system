type InspectionDetailProps = {
  inspectionId: string;
};

export function InspectionDetail({ inspectionId }: InspectionDetailProps) {
  return (
    <main>
      Inspection {inspectionId}: bounding boxes, segmentation masks, severity, confidence, and safety warning placeholders.
    </main>
  );
}
