import { InspectionDetail } from "@/features/inspections/InspectionDetail";

export default function InspectionDetailPage({ params }: { params: { id: string } }) {
  return <InspectionDetail inspectionId={params.id} />;
}
