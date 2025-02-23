import { TestBed } from '@angular/core/testing';

import { TitansService } from './Titans.service';

describe('TitansService', () => {
  let service: TitansService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TitansService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
