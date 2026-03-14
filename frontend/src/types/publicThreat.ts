export interface PublicThreatCard {
  title: string;
  severity: string;
  source: string;
  summary: string;
}

export interface ReviewItem {
  id: string;
  type: string;
  status: string;
  note: string;
}
