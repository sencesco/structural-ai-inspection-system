import { ReportDetail } from "@/features/reports/components/ReportDetail";

export default function ReportDetailPage({ params }: { params: { id: string } }) {
  return <ReportDetail reportId={params.id} />;
}
