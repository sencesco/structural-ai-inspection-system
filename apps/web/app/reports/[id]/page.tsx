import { ReportDetail } from "@/features/reports/ReportDetail";

export default function ReportDetailPage({ params }: { params: { id: string } }) {
  return <ReportDetail reportId={params.id} />;
}
